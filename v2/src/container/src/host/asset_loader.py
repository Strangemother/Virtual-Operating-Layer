import os


class AssetLoader(object):
    """Loading Functionality for the container caller connected to this runtime
    """

    def __init__(self, browser):
        self.browser = browser

    def askContainer(self, filepath, execute_function):
        print('Load', filepath)
        asset = os.path.join('assets', 'js', filepath)
        self.browser.ExecuteFunction(execute_function, asset)
        return filepath

def bind(browser):
    return ("assets", AssetLoader(browser),)
