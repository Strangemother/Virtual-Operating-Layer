# Hello world example. Doesn't depend on any third party GUI framework.
# Tested with CEF Python v55.3+.

from cefpython3 import cefpython as cef
import platform
import sys
import time
import winsound
from multiprocessing import Process
from http import server
import threading
import os
import base64


ROOT = os.path.normpath( os.path.join( os.path.dirname( os.path.abspath(__file__) ), '..') )

def beep(frequency=1400, duration=50):
    winsound.Beep(frequency, duration)


def set_global_handler():
    # A global handler is a special handler for callbacks that
    # must be set before Browser is created using
    # SetGlobalClientCallback() method.
    global_handler = GlobalHandler()
    cef.SetGlobalClientCallback("OnAfterCreated", global_handler.OnAfterCreated)


def set_client_handlers(browser):
    client_handlers = [ClientHandler()]
    for handler in client_handlers:
        browser.SetClientHandler(handler)


def set_javascript_bindings(browser):
    '''
    Write and bind JS hook functionality.
    '''

    bindings = cef.JavascriptBindings(
            bindToFrames=True,
            bindToPopups=True
            )
    #bindings.SetProperty("python_property", "This property was set in Python")
    #bindings.SetProperty("cefpython_version", cef.GetVersion())
    bindings.SetFunction("html_to_data_uri", html_to_data_uri)

    # external = External(browser)
    # bindings.SetObject("external", external)

    js_hooks = VOLJavascriptHook(browser)
    bindings.SetObject("VOL", js_hooks)
    browser.SetJavascriptBindings(bindings)
    # browser.ExecuteJavascript("setTimeout(function(){ console.log('timeout') }, 3000)")
    browser.ExecuteJavascript("console.log('Bound Javascript')")


def js_print(browser, lang, event, msg):
    # Execute Javascript function "js_print"
    browser.ExecuteFunction("js_print", lang, event, msg)


class GlobalHandler(object):

    def OnAfterCreated(self, browser, **_):
        """Called after a new browser is created."""
        # DOM is not yet loaded. Using js_print at this moment will
        # throw an error: "Uncaught ReferenceError: js_print is not defined".
        # We make this error on purpose. This error will be intercepted
        # in DisplayHandler.OnConsoleMessage.
        # js_print(browser, "Python", "OnAfterCreated", "This will probably never display as DOM is not yet loaded")
        # Delay print by 0.5 sec, because js_print is not available yet

        # threading.Timer(0.5, browser.ExecuteJavascript, ["console.log('OnAfterCreated');foo=1"]).start()
        # browser.ExecuteJavascript('window.foo=1')
        # browser.ExecuteJavascript("console.log('OnAfterCreated')")


class ClientHandler(object):
    def OnConsoleMessage(self, browser, message, **_):
        """Called to display a console message."""
        # This will intercept js errors, see comments in OnAfterCreated
        if "error" in message.lower() or "uncaught" in message.lower():
            # Prevent infinite recurrence in case something went wrong
            if "js_print is not defined" in message.lower():
                if hasattr(self, "js_print_is_not_defined"):
                    print("Python: OnConsoleMessage: "
                          "Intercepted Javascript error: "+message)
                    return
                else:
                    self.js_print_is_not_defined = True
            # Delay print by 0.5 sec, because js_print may not be
            # available yet due to DOM not ready.
            args = [browser, "Python", "OnConsoleMessage",
                    "(Delayed) Intercepted Javascript error: <i>{error}</i>"
                    .format(error=message)]
            threading.Timer(0.5, js_print, args).start()


    def OnLoadingStateChange(self, browser, is_loading, **_):
        """Called when the loading state has changed."""
        if not is_loading:
            # Loading is complete. DOM is ready.
            browser.ExecuteFunction('haio_in', "VOL::Loading complete")
            browser.ExecuteJavascript("console.log('apples')")


class VOLJavascriptHook(object):

    def __init__(self, browser):
        self.browser = browser

    def version(self):
        return 100

    def test_multiple_callbacks(self, js_callback):
        """Test both javascript and python callbacks."""
        # js_print(self.browser, "Python", "test_multiple_callbacks", "Called from Javascript. Will call Javascript callback now.")

        def py_callback(msg_from_js):
            js_print(self.browser, "Python", "py_callback", msg_from_js)
        if hasattr(js_callback, 'Call'):
            js_callback.Call("String sent from Python", py_callback)
        else:
            print('Recv', js_callback)


def html_to_data_uri(html, js_callback=None):
    # This function is called in two ways:
    # 1. From Python: in this case value is returned
    # 2. From Javascript: in this case value cannot be returned because
    #    inter-process messaging is asynchronous, so must return value
    #    by calling js_callback.
    html = html.encode("utf-8", "replace")
    b64 = base64.b64encode(html).decode("utf-8", "replace")
    ret = "data:text/html;base64,{data}".format(data=b64)
    if js_callback:
        # js_print(js_callback.GetFrame().GetBrowser(),
        #          "Python", "html_to_data_uri",
        #          "Called from Javascript. Will call Javascript callback now.")
        js_callback.Call(ret)
        return

    return ret


def start_container():
    check_versions()
    beep()
    sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error

    settings = dict(
        #"multi_threaded_message_loop": True,
        persist_user_preferences=True,
        product_version="nux.vol/0.1",
        user_agent="Nux VOL",
        cache_path=os.path.join(ROOT, "system", "cache"),
        downloads_enabled=True,
        # automated int
        remote_debugging_port=0,
        string_encoding='utf-8',
        user_data_path=os.path.join(ROOT, "system", "user_data"),
        app_user_model_id="nux.vol.0.1-service",
        debug=True,
        log_file=os.path.join(ROOT, 'system', 'debug.log'),
        locales_dir_path=os.path.join(ROOT, "system", "locales"),
        log_severity=cef.LOGSEVERITY_INFO,
        resources_dir_path=os.path.join(ROOT, 'system', 'resources'),
        #background_color=11000011,
    )

    commandLineSwitches = {
        'js-flags':"--expose-wasm",
        # 'show-fps-counter':'',
        # 'renderer':'',
        #'screenshot':'',
        #'enable-webvr':'',
        # 'enable-webvr': '',
        'javascript-harmony': '',
        'window-position': '100,2000',
        'window-size': '100,100',
        # https://msdn.microsoft.com/en-us/library/windows/desktop/dd370844.aspx
        #'enable-exclusive-audio': ''
    }

    set_global_handler()
    initialized = cef.Initialize(settings=settings, commandLineSwitches=commandLineSwitches)
    beep()

    browser = cef.CreateBrowserSync(
        # url="file:///C:/Users/jay/Documents/projects/desktop/vol/foo.html",
        url="http://localhost:9010",
        settings=dict(
            universal_access_from_file_urls_allowed=True,
            file_access_from_file_urls_allowed=True,
            #background_color=11000000,
            javascript_access_clipboard_disallowed=False,
            ),
        window_title="nux vol"
        )
    set_client_handlers(browser)
    set_javascript_bindings(browser)

    cef.MessageLoop()

    print('Shutting down')
    beep(1000)
    time.sleep(1)

    cef.Shutdown()
    beep(1000)


def start_vol():
    run_server(server.HTTPServer, server.SimpleHTTPRequestHandler)


def run_server(server_class, handler_class):
    server_address = ('', 9010)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


def main():

    # return start_container()

    cont_proc = Process(target=start_container)
    cont_proc.start()

    http_proc = Process(target=start_vol)
    http_proc.start()

    cont_proc.join()
    http_proc.terminate()
    print('Close')


def check_versions():
    print("CEF Python {ver}".format(ver=cef.__version__))
    print("Python {ver} {arch}".format(ver=platform.python_version(), arch=platform.architecture()[0]))
    assert cef.__version__ >= "55.3", "CEF Python v55.3+ required to run this"


if __name__ == '__main__':
    main()
