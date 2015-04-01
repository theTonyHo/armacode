AddLayer
--------

.. py:Function:: AddLayer(name=None, color=None, visible=True, locked=False)


Add a new layer to the document.
Extended from Rhinoscript syntax with Full Layer name support
Parent Layer automatically added if does not exist.
:param name[opt]: The full path of the new layer. If omitted, Rhino automatically
                  generates the layer name.
:param color[opt]: A Red-Green-Blue color value or System.Drawing.Color. If
                   omitted, the color Black is assigned.
:param visible[opt]: layer's visibility
:param locked[opt]: layer's locked state

:returns: The full name of the new layer if successful.