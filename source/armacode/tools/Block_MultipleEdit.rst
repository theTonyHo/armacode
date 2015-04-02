
Tool Name: ``Block_MultipleEdit``

.. index:: Block_MultipleEdit (Tool)

.. _tools.block_multipleedit:

Block Multiple Edit.
Similar to BlockEdit command, applying on multiple block instances at once.
Selected instances must be a unique instance of a definition.
Explode all blocks and lock all other objects.
Once done. Run the script again to update the modified geometries.
Limited to Modify and Delete.
Adding object is possible by assigning a UserText value of the parent block id
To add object to block, use the builtin BlockEdit method. This is because adding objects require selection of a specific block.