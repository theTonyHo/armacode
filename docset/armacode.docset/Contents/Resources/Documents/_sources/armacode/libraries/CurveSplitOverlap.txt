CurveSplitOverlap
-----------------

.. py:Function:: CurveSplitOverlap(curve_IDs, tolerance=None)


Detect overlapping of curves and split
:param curve_IDs = Input Curve GUIDs:
:param tolerance [opt] = Tolerance for intersection. If None, document tolerance is used:

:returns: identifier of the splitted curves on success
          input curves on error.