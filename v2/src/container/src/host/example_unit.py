"""An example unit

A Simple unit requires an exposed 'bind' method, returning a name
and an instance of your unit.
The given 'browser' hooks the incoming interface, to keep longterm
for UI feedback.

class Example(object):
    pass

def bind(browser):
    return ('example', Example(browser), )
"""
import os

print('ExampleUnitItem')

class ExampleUnitItem(object):
    """Loading Functionality for the
    container caller connected to this runtime"""

    def __init__(self, browser):
        self.browser = browser

    def apple_cake(self, *items, execute_function='js_print'):
        print('example cake:', items)
        asset = os.path.join('assets', 'js', filepath)
        self.browser.ExecuteFunction(execute_function, asset)
        return filepath

def bind(browser):
    return ("example", ExampleUnitItem(browser),)
