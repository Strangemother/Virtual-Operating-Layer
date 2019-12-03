from cefpython3 import cefpython as cef
from multiprocessing import Process, Queue
import os
import platform
import sys
import time
import winsound

HOST = 'localhost'
PORT = 8093

import manifest
import settings

def beep(frequency=1400, duration=100):
    winsound.Beep(frequency, duration)


def start_container(home, handlers=None, callback=None):
    #global MANIFEST
    beep()
    os.chdir(home)
    check_versions()
    #MANIFEST = settings.resolve(home)
    sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error
    cef.Initialize()
    browser = cef.CreateBrowserSync(url="file://{}/index.html".format(home),
        window_title="VOL")

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
