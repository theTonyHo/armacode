UnfoldBrepAuto
--------------

.. py:Function:: UnfoldBrepAuto(brep_id, *staticIndices)


Automatically Unfold a Brep with a set of static face indices.

Generate one sequence at a time.
Working with Static, Remaining Indices.
Associate all remaining faces to the immediate level. i.e. adjacent faces of the current static face.

The order off association is calculated by the order of the face indices.
It is best to have important faces with the lowest index. I.e. Most obvious base static face should have index of 0.

:param brep_id: Indentifier of the brep to unfold.
:param staticIndices: Index of each static face as separate parameter.

:returns: Unfolded Brep on success. Unfold progress may stop at ambiguous solutions.
