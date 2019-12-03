from cefpython3 import cefpython as cef
from multiprocessing import Process, Queue
from pexpect.popen_spawn import PopenSpawn
import os
import platform
import sys
import time
import winsound

HOST = 'localhost'
PORT = 8093

def main():
    path = os.path.abspath(os.path.dirname(__file__))
    home = os.path.join(path, 'home')
    # os.chdir(home)
    # global session
    #session = term_main('main', callback=callback)
    global browser
    session = {'name': 'main', 'app': 'cmd', 'early': ()}

    pc = PopenSpawn(session['app'])

    browser, cef = start_container(home, [LoadHandler()])
    set_javascript_bindings(browser, cef)
    print('Loaded.')

    print('Shutting down')
    cef.Shutdown()

def set_javascript_bindings(browser, cef):
    external = External(browser)
    bindings = cef.JavascriptBindings(
            bindToFrames=False, bindToPopups=False)
    bindings.SetProperty("python_property", "This property was set in Python")
    bindings.SetProperty("cefpython_version", cef.GetVersion())
    bindings.SetFunction("wake_ready", wake_ready)
    bindings.SetFunction("sessionInput", session_input)
    bindings.SetObject("external", external)
    browser.SetJavascriptBindings(bindings)


    # http_proc = Process(target=start_vol)
    # http_proc.start()
    #cont_proc.join()
    #http_proc.join()

def beep(frequency=1400, duration=100):
    winsound.Beep(frequency, duration)


def start_container(home, handlers=None, callback=None):
    beep()
    os.chdir(home)
    check_versions()
    sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error
    cef.Initialize()

    browser = cef.CreateBrowserSync(url="file://{}/index.html".format(home),
        window_title="Terminal")

    set_client_handlers(browser, handlers=handlers)

    return browser, cef

    # cef.MessageLoop()
    # cef.Shutdown()
    # print('Shutting down')
    # time.sleep(1)


def set_client_handlers(browser, handlers=None):
    handlers = handlers or []
    client_handlers = [] + handlers#, DisplayHandler()]
    for handler in client_handlers:
        browser.SetClientHandler(handler)


def check_versions():
    print("CEF Python {ver}".format(ver=cef.__version__))
    print("Python {ver} {arch}".format(
        ver=platform.python_version(), arch=platform.architecture()[0]))
    assert cef.__version__ >= "55.3", "CEF Python v55.3+ required to run this"


def proc_start(home, handlers=None, callback=None):
    os.chdir(home)
    queue = Queue()
    cont_proc = Process(target=start_container, args=(home, handlers, queue, callback,))
    #cont_proc = start_container(home, handlers, callback,)
    cont_proc.start()
    return cont_proc,queue

if __name__ == '__main__':
    main()
