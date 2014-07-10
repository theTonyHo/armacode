ObjectNameFromAttributes
------------------------
Evaluate a formatted string by retrieving the values from User Text Attributes
The string format needs to contain fields referencing other attributes.
For example: an object should contain the following as attributes.
    NAME_FORMAT: {NAME}_{INDEX}
    NAME: WP
    INDEX: 002

    This will return a string WP_002. Refer to the wiki page




:returns: A string representing a new name on success. None on error.