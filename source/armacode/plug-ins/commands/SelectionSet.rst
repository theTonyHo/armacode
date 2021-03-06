.. index:: SelectionSet (Command)

.. _selectionset_cmd:

SelectionSet
------------
Selection Sets
Stored search queries for objects selection.
It is useful to group object selection by creating a selection set.
Selection Set entry is stored as Document Data with a prefix SelectionSet.

Filter:
    Create a selection set by filtering object attributes. The following options are commonly used:

        name: * .Filter by Name
        layerName: * Filter by Layer name (Full Path)
        layout: * Filter by Layout name
        filter: 0 Filter by type. Refer to rs.filter type values.

    User Text key/value pairs can also be included in the query
    <key>: <value>
    More than one UserText key/value pair can be filtered. Note only usertext attached to attributes are searched.

Save:
    Create a selection set with the current object selection. Object_IDs are stored/included as a special filter in the query.
    Current Method:
        Set Query to contain a custom filter OBJECT_IDS with all GUIDs of selected objects as value.
        This method allows an object to belong to MULTIPLE Selection Set.
    Attempted Method:
        Set custom UserText key/value on Selected Objects.
        On saving a selection set, a key/value pair of "SelectionSet" as key and the newly created selection set name as value is stored on the selected objects.
        This method only allow an object to belong to ONE Selection Set.

Restore:
    Restore a previously saved Selection set. Does not deselect.

Delete:
    Remove a selection set entry from the document.