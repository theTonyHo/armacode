Logger
------

.. py:Function:: Logger(loggerName=None, fileName=None, console=False, resetHandlers=False)


Instantiate a logger object with default Formatter.
Default level is set to WARNING (based on the root logger)

:param loggerName: Name of the logger. Usually __file__ or something sensible.
:param fileName: File name of the log file. If ommitted, logger will default to console
:param console: Display in console. Specify
:param resetHandlers: Set this to True to clear all existing handlers.

:returns: Logger Object

.. rubric:: Example

import armacode
logger = armacode.Logger(__file__)
logger.debug("This is a debug message")

Reference:
    http://stackoverflow.com/questions/13733552/logger-configuration-to-log-to-file-and-print-to-stdout