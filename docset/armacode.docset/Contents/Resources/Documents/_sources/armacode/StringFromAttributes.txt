StringFromAttributes
--------------------

.. py:Function:: StringFromAttributes(object_id, strFormat=None)


Set an object name by evaluating a formatted string
The string format needs to contain fields referencing other attributes.
Fields provided in the formatted string are substrituted by the values from User Text Attributes





:returns: A string representing a new name on success. None on error.

.. rubric:: Notes

An object should contain the following as attributes.::

    NAME_FORMAT: {NAME}_{INDEX}
    NAME: WP
    INDEX: 002

This will return a string ``WP_002``. Refer naming automation workflow.
