#from loguru import logger
import sys

# > import coloredlogs, logging
# > coloredlogs.install()
# > logging.info("It works!")
# 2014-07-30 21:21:26 peter-macbook root[7471] INFO It works!

try:
    import coloredlogs
except ImportError:
    print('no coloredlogs, condider installing coloredlogs')
    coloredlogs = None

import logging
# # Create a logger object.
# filename='example.log', filemode='w',
logging.basicConfig(level=logging.DEBUG, format=' - {message}', datefmt='%H:%M:%S ', style='{')
logger = logging.getLogger(__name__)
# level = logging.getLevelName('DEBUG')
# logger.setLevel(level)

try:
    from termcolor import colored
except ImportError:
    colored = None



# logger.add(sys.stdout, colorize=True,
#     format="<green>{time}</green> {message}")
#LOG_FORMAT='%(asctime)s %(process)d %(levelname)s %(message)s'
LOG_FORMAT='%(levelname)s %(message)s'

DEFAULT_LEVEL_STYLES = {
    'critical': { 'color': 'red', 'bold': True},
    'debug': {'color': 'green'},
    'error': {'color': 'red'},
    'info': {},
    'notice': {'color': 'magenta'},
    'spam': {'color': 'green', 'faint': True},
    'success': {'color': 'green', 'bold': True},
    'verbose': {'color': 'blue'},
    'warning': {'color': 'yellow'}
}


# By default the install() function installs a handler on the root logger,
# this means that log messages from your code and log messages from the
# libraries that you use will all show up on the terminal.

if coloredlogs is not None:
    # If you don't want to see log messages from libraries, you can pass a
    # specific logger object to the install() function. In this case only log
    # messages originating from that logger will show up on the terminal.
    coloredlogs.install(level='DEBUG', fmt=LOG_FORMAT,
                        datefmt='%H:%M:%S',
                        logger=logger, level_styles=DEFAULT_LEVEL_STYLES)


# Some examples.
logger.debug("this is a debugging message")
logger.info("this is an informational message")
logger.warning("this is a warning message")
logger.error("this is an error message")
logger.critical("this is a critical message")

def log(lvl, *a, color=None, method='log'):
    """
        >>> import log;log.log('there is no spoon')
        03:45:22 13240 INFO there is no spoon
        >>> log.log(40, 'there is no spoon')
        03:45:24 13240 ERROR there is no spoon
        >>> log.log('there is no spoon', color='white')
        03:46:07 13240 INFO there is no spoon
    """
    if isinstance(lvl, str):
        a = (lvl,) + a
        lvl = 20

    r = ''.join(map(str, a))
    if color:
        r = colored(r, color)
    getattr(logger, method)(lvl, r)

log.debug = logger.debug
log.info = logger.info
log.warning = logger.warning
log.warn = logger.warning
log.error = logger.error
log.critical = logger.critical
log.log = logger.log

if colored is None:
    print('No color logging. Consider installing termcolor')
    colored = lambda x,c: log.log(x)
