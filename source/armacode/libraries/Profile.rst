Profile
-------

.. py:Function:: Profile(fn)


Profile decorator.
Place this above the function to monitor its usage. Then use DebugFunctionProfile to display usage information.
REFERENCE: http://stackoverflow.com/questions/3620943/measuring-elapsed-time-with-the-time-module

For Example:

import armacode

@armacode.Profile
def your_function():
    for i in range(1000):
        print i

if __name__ == "__main__":
    your_function()
    armacode.DebugFunctionProfile()