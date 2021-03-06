Global Variables
================

    armacode has global settings which can can be configured by modifying ``armacode.ini`` to the user's preference.


.. py:data:: armacode.debug

bool : Useful during the development of a script.

.. py:data:: armacode.parallel
bool : Toggle multithreading on or off globally.

.. py:data:: armacode.logfile
str : Location of the global log file.

.. py:data:: armacode.defaultColors
list[color] : List of default low-saturation colors

To use the new settings, Rhino Python scripting engine needs to be reset. This can be achieved by ``_RunPythonScript ResetEngine``


User Configuration Settings
===========================

Settings can be stored and retrieved inside any script or tools. These are different to ``Sticky``, stored in memory, as they are stored permanently in a setting (.ini) file.

Scripts should attempt to retrieve the settings before revert to default hardcoded settings.

Scripts should save the settings to the file on successful operation.

Settings consist of **Sections**, **Option** and **Value** pair.

**Section**

Stored settings should be put under a recognisable unique Section name.

**Option/Value** Pair

Name and value of the option


Set value to Settings
---------------------

Values can be set to sticky by calling the :py:func:`armacode.config.SetOption` function.


Get value from Settings
-----------------------

Stored values can be retrieved from sticky by calling the :py:func:`armacode.config.GetOption` function.


Save Settings to configuration (.ini) file
------------------------------------------

Stored settings in armacode.config can be saved to file by calling :py:func:`armacode.config.Save` function.


Example
-------

.. literalinclude:: ./UserConfiguration.py
    :linenos:
    :language: python


