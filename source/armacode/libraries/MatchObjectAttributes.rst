MatchObjectAttributes
---------------------

.. py:Function:: MatchObjectAttributes(target_ids, source_id=None)


Matches, or copies the attributes of a source object to a target object. Retains the User Strings data.
Objects on Reference layer will have their layer name truncated and added to document.
Also work with objects inside a block definition.

:param target_ids = identifiers of objects to copy attributes to:
:param source_id[opt] = identifier of object to copy attributes from. If None,:
:param then the default attributes are copied to the target_ids:

:returns: number of objects modified

.. rubric:: Example

.. code :: python

    import rhinoscriptsyntax as rs
    import armacode

    obj = rs.GetObjects("Select Objects to match attributes")
    sourceObj = rs.GetObject("Source object to match attributes to")

    if obj and sourceObj:
        armacode.MatchObjectAttributes(obj, sourceObj)
