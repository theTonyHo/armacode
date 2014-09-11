StickyGet
---------

.. py:function:: StickyGet(name, *keys)


Get the settings with named key that was stored in the scriptcontext sticky.

:param name: Provide a name where all the settings will sit under. This is to separate settings from scripts.
:param keys: name of the variable to retrieve. Multiple keys are supported.


:returns: If one key is provided.

          Value List : If keys provided, list of values for corresponding key. Value is returned None if not found.

          Value Dictionary : If keys not specified, a dictionary of all settings is returned.
:rtype: Value
