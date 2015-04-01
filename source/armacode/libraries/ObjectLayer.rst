ObjectLayer
-----------

.. py:Function:: ObjectLayer(object_id, layer=None)


Returns or modifies the layer of an object
:param object_id = the identifier of the object(s):
:param layer[opt] = name of an existing layer:

:returns: If a layer is not specified, the object's current layer
          If a layer is specified, the object's previous layer
          If object_id is a list or tuple, the number of objects modified