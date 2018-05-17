DebugFunctionProfile
--------------------

.. py:Function:: DebugFunctionProfile()


Display profiling information of a recently called function. Only in Debug mode only.

:returns: 0: Number of times the function has been executed.
          1: Previous run time.
          2: Execution max time
          3: Average Time
:rtype: A List of profiling data

REFERENCE: http://stackoverflow.com/questions/3620943/measuring-elapsed-time-with-the-time-module

Format:
    Function your_function called 6 times.
    Execution time max: 1.454, average: 1.431