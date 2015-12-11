BrepEdges
---------

.. py:Function:: BrepEdges(object_id, as_CurveObjects=True)


Extract Brep Edges

:param object_id: object extract edges from
:param as_CurveObjects[opt]: Return as Curve Objects if True. Otherwise return BrepEdge objects.

:returns: Naked, Interior, NonManifold, ValleyFold, and ValleyFold.Each key has an associated list of geometry.

:rtype: dictionary with keys
