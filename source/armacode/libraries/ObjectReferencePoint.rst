ObjectReferencePoint
--------------------

.. py:Function:: ObjectReferencePoint(object_id, pull=True)


Evaluate a reference point for a object.
Reference point is a point indicate where the object is in model space.
It is calculated by the center of the bounding box in World XY Plane.
If pull is set to True, and an object is a Block instance, the insertion point is returned.
:param object_id: Identifier of an object.
:param pull: Optional, If True, the point is pulled to sit on the object.

:returns: point in World coordinates.
