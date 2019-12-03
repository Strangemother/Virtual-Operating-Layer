import subprocess
from pexpect.popen_spawn import PopenSpawn
from pexpect import exceptions
from multiprocessing import Process, Queue
import queue as Q
from time import sleep
from log import get_logger
import threading

logger = get_logger()
sessions = {}


def main(name='main', callback=None):
    session = create(name, proc_target=cmd_process, callback=callback)
    return start(session)

def printer_callback(session, string):
    log(string)

def create(name, proc_target, callback=None):
    log('enter')
    cmd_q = Queue()
    com_q = Queue()
    ret_q = Queue()
    lock = None  #threading.Lock()
    t = threading.Thread(
        target=pump_worker, args=(name, com_q, lock, sessions, callback))
    p = Process(target=proc_target, args=(cmd_q, ret_q, com_q, callback))

    session = {
        'pump': True,
        'process': p,
        'name': name,
        'cmd_q': cmd_q,
        'com_q': com_q,
        'ret_q': ret_q,
    }

    if name in sessions:
        del sessions[name]
    sessions[name] = session
    session['pump'] = t

    return session


def start(session):
    session['process'].start()
    log('Waiting for cmd response')
    log("... Done", session['ret_q'].get())
    session['pump'].start()
    return session


def block():
    join(session)
    return close(session)


def close(session):
    log('stop')
    session['cmd_q'].put('TEXIT')
    session['com_q'].put('TEXIT')
    log('...Done', session['com_q'].get())
    log('finish')
    return session


def join(session):
    try:
        log('SESSION JOIN')
        if session['process'] is not None:
            session['process'].join()
        if session['pump'] is not None:
            session['pump'].join()
    except KeyboardInterrupt:
        log('SESSION CLOSE')
    del session['process']
    del session['pump']


def send(cmd, wait=False, session=None, callback=None):
    #log('sending', cmd)
    session = session or sessions['main']
    if isinstance(session, (str,)):
        session = sessions.get(name, None)

    if session is None:
        log('Failure for send() to', session)
        return False

    session['cmd_q'].put(cmd)
    if wait:
        sleep(.2)
        return pump(session, 2, callback)


def pump(session=None, count=1, callback=None):
    session = session or sessions['main']
    run = count
    pumped = False
    while run:
        dlog('*')
        string = ''
        try:
            string = session['ret_q'].get_nowait()
        except Q.Empty:
            pass
        run -= 1
        if len(string) > 0:
            dstr = string.decode('utf') if hasattr(string,
                                                   'decode') else string
            # log('Return', dstr)
            # print(dstr, end='')
            if callback is not None:
                callback(session, dstr)
            pumped = True
        else:
            run = 0
    dlog('|')
    return pumped


def log(*strings):
    logger.info(' '.join(map(str, strings)))


def dlog(*a):
    pass


def cmd_process(cmd_q, rq, com_q, callback=None, step_func=None):
    pc = PopenSpawn('winpty/bin/winpty.exe cmd')
    run = 1
    log('Response')
    rq.put('RUN')
    log('Run')

    while run:
        command = ''
        try:
            command = cmd_q.get_nowait()
        except Q.Empty:
            pass

        if len(command) > 0:
            dlog('>', command)
            if command == 'TEXIT':
                log('KILL COMMAND HOST')
                command = 'exit'
            pc.sendline(command)
        try:
            string = pc.read_nonblocking(size=1024, timeout=1)
        except exceptions.EOF as e:
            #End Of File (EOF).
            log('Command process terminal exiting due to EOF', command)
            run = 0
            rq.put_nowait('EOF')
            com_q.put_nowait('EOF')

        if len(string) == 0:
            dlog('_')
            try:
                sleep(.1)
            except KeyboardInterrupt as e:
                log('Close Command Process')
                run = 0
                rq.put_nowait('TEXIT')
                com_q.put_nowait('TEXIT')
            dlog('^')
            continue
        if step_func is not None:
            step_func(string)

        if (len(command) > 0) and hasattr(cmd_q, 'task_done'):
            cmd_q.task_done()

        dlog("<", len(string))
        rq.put_nowait(string)
        dlog('.')

    log('End of process')


def pump_worker(name, com_q, lock, sessions, callback=None):
    """thread pump_worker function"""
    run = 1
    while run:
        command = ''
        try:
            command = com_q.get_nowait()
        except Q.Empty:
            pass

        if len(command) > 0:
            # log('>', command)
            if command in ['TEXIT', 'EOF']:
                log('KILL COMMAND HOST', command)
                run = 0

        #lock.acquire()
        pumped = pump(sessions[name], callback=callback)
        #lock.release()
        if sessions[name]['pump'] is False:
            run = 0
            continue
        if pumped is False:
            sleep(.2)
        dlog('-')

    log('Close pump')
    com_q.put('TEXIT')


if __name__ == '__main__':
    session = main()
