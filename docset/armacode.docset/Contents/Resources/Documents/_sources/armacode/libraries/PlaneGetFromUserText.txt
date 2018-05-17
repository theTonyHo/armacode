PlaneGetFromUserText
--------------------

.. py:Function:: PlaneGetFromUserText(object_id, key='PLANE')


Get Plane information from User Text attribute stored in an object.
Stored Plane can be GUID of a Rhino Object containing plane information. For example, surfaces, Text, etc.
Otherwise it must be in one of the following format:

"Origin=0,0,0 XAxis=1,0,0, YAxis=0,1,0, ZAxis=0,0,1" This is default string representation of a Plane in Python.
"O(0,0,0) X(1,0,0) Y(0,1,0)" Short customised version. OXY is sufficient to rebuild the plane.

    Args:
        object_id: Id of object to set.
        key: Optional. Specify the Usertext key to get value from.

    Returns:
        Plane object on success.