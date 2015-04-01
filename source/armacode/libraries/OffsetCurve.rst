OffsetCurve
-----------

.. py:Function:: OffsetCurve(object_id, plane, distance, bothside=0, cornerStyle=1, capStyle=0)


Offsets a curve by a distance. The offset curve will be added to Rhino if the input is guid.
Extended from rhinoscript syntax to allow bothside and capping style.

:param object_id = Identifier of a curve object. Can be a curve object (compatible with Grasshopper):
:param plane = Plane to offset on:
:param distance = Distance of the offset:
:param cornerStyle[opt] = the corner style:
                                            0 = None, 1 = Sharp, 2 = Round, 3 = Smooth, 4 = Chamfer
:param capStyle[opt] = capping style:
                                      0 = None, 1 = Flat, 2 = Round


:param List of ids for the new curves on success:
:param None on error:
