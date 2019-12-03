

INTERRUPT = (
    'Exception'
    , 'KeyboardInterrupt'
    , 'NotImplemented'
    , 'StopIteration'
    , 'GeneratorExit'
    , 'StopAsyncIteration'
    , 'SystemExit'
    , 'TaskletExit'
)


ERROR = (
    'ArithmeticError'
    , 'AssertionError'
    , 'AttributeError'
    , 'BaseException'
    , 'BlockingIOError'
    , 'BrokenPipeError'
    , 'BufferError'
    , 'ChildProcessError'
    , 'ConnectionAbortedError'
    , 'ConnectionError'
    , 'ConnectionRefusedError'
    , 'ConnectionResetError'
    , 'EOFError'
    , 'EnvironmentError'
    , 'FileExistsError'
    , 'FileNotFoundError'
    , 'FloatingPointError'
    , 'ImportError'
    , 'IndentationError'
    , 'IndexError'
    , 'InterruptedError'
    , 'IsADirectoryError'
    , 'KeyError'
    , 'IOError'
    , 'LookupError'
    , 'MemoryError'
    , 'ModuleNotFoundError'
    , 'PermissionError'
    , 'ProcessLookupError'
    , 'RecursionError'
    , 'ReferenceError'
    , 'RuntimeError'
    , 'NameError'
    , 'NotADirectoryError'
    , 'NotImplementedError'
    , 'OSError'
    , 'OverflowError'
    , 'SyntaxError'
    , 'SystemError'
    , 'TimeoutError'
    , 'TypeError'
    , 'UnboundLocalError'
    , 'UnicodeDecodeError'
    , 'UnicodeEncodeError'
    , 'UnicodeError'
    , 'UnicodeTranslateError'
    , 'ValueError'
    , 'WindowsError'
    , 'ZeroDivisionError'
    , 'TabError'
)


WARNING = (
    'BytesWarning'
    , 'DeprecationWarning'
    , 'FutureWarning'
    , 'ImportWarning'
    , 'UserWarning'
    , 'PendingDeprecationWarning'
    , 'ResourceWarning'
    , 'RuntimeWarning'
    , 'SyntaxWarning'
    , 'UnicodeWarning'
    , 'Warning'
)


COMPLEX =(
    '_'
    , '__build_class__'
    , '__debug__'
    , '__doc__'
    , '__import__'
    , '__loader__'
    , '__name__'
    , '__package__'
    , '__spec__'
)


MATH = (
    'abs'
    , 'max'
    , 'min'
    , 'divmod'
    , 'pow'
    , 'range'
    , 'complex'
    , 'round'
    , 'sum'
)


STRING = (
    'ascii'
    , 'ord'
    , 'bin'
    , 'chr'
    , 'str'
)


TYPE = (
    'int'
    , 'float'
    , 'bool'
    , 'True'
    , 'False'
    , 'None'

    , 'tuple'
    , 'set'
    , 'list'
    , 'object'
    , 'dict'

    , 'Ellipsis'

    , 'hex'
    , 'oct'
    , 'bytes'
    , 'bytearray'
)


CLASS = (
    'type'
    , 'super'
    , 'classmethod'
    , 'frozenset'
    , 'callable'
    , 'property'
    , 'isinstance'
    , 'issubclass'
    , 'staticmethod'
)


LIB = (
    'setattr'
    , 'getattr'
    , 'delattr'
    , 'hasattr'
    , 'hash'
    , 'id'
    , 'len'
    , 'dir'
)


FUNCTION = (
    'compile'
    , 'eval'
    , 'input'
    , 'exec'
    , 'globals'
    , 'locals'
)


ITER = (
    # Iteration
    'enumerate'
    , 'next'
    , 'zip'
    , 'iter'
    , 'filter'
    , 'all'
    , 'format'
    , 'reversed'
    , 'any'
)


HELPER = (
    #help
    'repr'
    , 'sorted'
    , 'vars'
    , 'dir'
    , 'slice'

    # File
    , 'open'
    , 'map'
    , 'memoryview'

    , 'help'
    , 'print'
)


ROOT = INTERRUPT + TYPE + STRING + CLASS + LIB
PRIMARY = ERROR + WARNING + MATH + FUNCTION + ITER
SECONDARY = COMPLEX + HELPER
