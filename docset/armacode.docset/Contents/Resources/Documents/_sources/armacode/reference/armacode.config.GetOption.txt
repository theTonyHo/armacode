armacode.config.GetOption
-------------------------

.. py:Function:: armacode.config.GetOption(self, section, key, returnType='str')


Get option from the config.

:param section: Section name of the setting
:param key: Name of the option
:param returnType: String describing the type of data to return. See below
                   str : String
                   bool : Boolean
                   int : Integer

Returns: Value if found. None on failure.