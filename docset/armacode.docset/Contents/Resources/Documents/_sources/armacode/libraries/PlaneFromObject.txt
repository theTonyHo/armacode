PlaneFromObject
---------------

.. py:Function:: PlaneFromObject(object_id)


Return a plane based on the type of object.
Polyline Curve, 3 points, XAxis aligned to the vector of the last segment.
Planar Curve: Approximated plane of planar curve.
Surface : Evaluated at normalised parameter (0.5,0.5)
Block Instance : Block instance base plane.
Text : Plane of Text object
Point : Single Point with current CPlane.