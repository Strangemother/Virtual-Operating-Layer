# Hello world example. Doesn't depend on any third party GUI framework.
# Tested with CEF Python v55.3+.

from cefpython3 import cefpython as cef
import platform
import sys
import time
import winsound
from multiprocessing import Process
from http import server

HOST = 'localhost'
PORT = 8093

def beep(frequency=1400, duration=100):
    winsound.Beep(frequency, duration)

def start_container():
    beep()
    check_versions()
    sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error
    cef.Initialize()
    cef.CreateBrowserSync(url="http://{}:{}".format(HOST, PORT),
                          window_title="nux vol")
    cef.MessageLoop()
    cef.Shutdown()
    print('Shutting down')
    time.sleep(1)

def start_vol():
    run_server(server.HTTPServer, server.SimpleHTTPRequestHandler)

def run_server(server_class, handler_class):
    beep()
    server_address = (HOST, PORT)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Close by keyboard')


def main():
    cont_proc = Process(target=start_container)
    cont_proc.start()

    http_proc = Process(target=start_vol)
    http_proc.start()

    cont_proc.join()
    http_proc.join()

def check_versions():
    print("CEF Python {ver}".format(ver=cef.__version__))
    print("Python {ver} {arch}".format(
          ver=platform.python_version(), arch=platform.architecture()[0]))
    assert cef.__version__ >= "55.3", "CEF Python v55.3+ required to run this"


if __name__ == '__main__':
    main()
