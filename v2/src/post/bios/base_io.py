
class IO:

    def __init__(self):
        print('wake IO')
        self.record_io()

    def record_io(self, root_fileno=100):
        io_d = dict()

        _found_atty = False
        print('Recording IO')
        for _fileno in range(0, root_fileno + 1):
            try:
                io_d[_fileno] = (os.isatty(_fileno), os.stat(_fileno), )
            except OSError:
                break
        stdio = (sys.stdin, sys.stdout, sys.stderr,)
        print('discovered {} BASE IO'.format(len(io_d)))

        writable = dict()
        print('Testing for Output')
        for io in stdio:

            if io.writable() is False:
                continue

            iof = io.fileno()
            #print('discovered', iof, io.name)
            iodo = io_d[iof]
            writable[iof] = io

            #print('discovered', iof, io.name, 'isatty', iodo[0])
            if ('out' in io.name) and (iodo[0] is True):
                #print('Found IO out hook item', iodo[1])
                self.hook(io, iodo[1])
                _found_atty = True

        if _found_atty is False:
            print('Attempting any IO Hook')
            for num in writable:
                item = writable[num]
                # print('Looking at', item, sys.stdout)
                if  sys.stdout == item:
                    iodo = io_d[item.fileno()]
                    self.hook(item, iodo[1])
                _found_atty = True


    def hook(self, stdio, stat):
        global puts
        self.stdout = stdio
        puts = self.print_hook# self.stdout.write
        puts(BEEP + 'Hello Spoon')

    def print_hook(self, *a, newline=None, level=1):
        if HEADER is not None:
            if HEADER.get('debug') is False and level > 1:
                # silence
                return

        self.stdout.write(' '.join(map(str, a)) + '\n')


