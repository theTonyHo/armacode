ExplodeBlockInstance
--------------------

.. py:method:: ExplodeBlockInstance(block_id, onlyVisible=False)


Explode Block Instance recursively to a list of geometries.
Block in worksession files are also supported. Objects inside the block will retain their layer structure.

:param block_id: Identifiers of block object
:param onlyVisible: Optional. If set to True, only copy visible objects.

:returns: List of exploded objects.