LinkToObject
------------

.. py:Function:: LinkToObject(object_ids, linkObject_id, key='LINKED_OBJECT')


Link multiple objects to another object using User Text Attributes.
All objects will have a User Attribute with key and Id of Link Object as value.
This is useful for identifying another object with direct relationship.

:param object_ids: Identifiers of objects to apply
:param linkObject_id: Identifier of the object to link with.
:param key: Name of the key to associate with

:returns: (int) Number of objects applied.
