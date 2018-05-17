GetUserText
-----------

.. py:Function:: GetUserText(object_id, key=None, attached_to_geometry=False)


Returns user text stored on an object.
:param object_id = the object's identifies:
:param key[opt] = the key name. If omitted all key names for an object are returned:
:param attached_to_geometry[opt] = location on the object to retrieve the user text.:

:returns: if key is specified, the associated value if successful
          if key is not specified, a dictionary of all user text key and values associated with the location.
