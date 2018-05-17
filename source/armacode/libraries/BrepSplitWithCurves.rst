BrepSplitWithCurves
-------------------

.. py:Function:: BrepSplitWithCurves(brep_id, curve_ids, delete_input=False)


Splits a brep with a list of curves.

:param brep_id: Identifier of the brep to split.
:param curve_ids: Identifiers of the curves to split the brep with.
:param delete_input: Delete the input identifier if True.

:returns: List of Identifiers of the new brep faces on success. If a brep geometry is provided, a modified brep is returned .
