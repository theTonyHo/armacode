wraps
-----

.. py:Function:: wraps(wrapped, assigned=('__module__', '__name__', '__doc__'), updated=('__dict__',))


Decorator factory to apply update_wrapper() to a wrapper function

Returns a decorator that invokes update_wrapper() with the decorated
function as the wrapper argument and the arguments to wraps() as the
remaining arguments. Default arguments are as for update_wrapper().
This is a convenience function to simplify applying partial() to
update_wrapper().