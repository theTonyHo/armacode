CreaseAngle
-----------

.. py:Function:: CreaseAngle(srfA, srfB, normalSegment=1)


Calculate the crease angle between two surfaces. The angle segment is determined by the surface normal.

:param srfA: Surface A
:param srfB: Surface B
:param normalSegment: If set to True, return the angle segment on the surface normal first. If set to False, return the smallest angle first

:returns: Common Edge Curve ID, Angle and its Reflex Angle.