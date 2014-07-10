StickyGet
---------
Get the settings with named key that was stored in the scriptcontext sticky
:param sectionName: Provide a name where all the settings will sit under. This is to separate settings from scripts.
:param keys: name of the variable to retrieve. Multiple keys are supported.

:returns: Value if sucessful. List of values if multiple keys are specified.
          None if not found.