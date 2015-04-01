UnfoldBrep
----------

.. py:Function:: UnfoldBrep(brep_id, indexA, indexB, *otherIndices)


Unfold a Polysurface by providing face indices.

:param brep_id: Brep or Identifier of Brep to unfold.
:param indexA: Index of Base Brep Face. (Static)
:param indexB: Index of Target Brep Face
:param otherIndices: Additional Indices of faces to unfold together with target face.


:returns: Unfolded Brep geometry. If Identifier is provided, the object is modified and identifier is returned.
:rtype: brep
