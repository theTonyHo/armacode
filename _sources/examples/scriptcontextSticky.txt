Scriptcontext Sticky
====================

    Script variables can be stored in the memory and retrieved later using ``scriptcontext.sticky``

``scriptcontext.sticky`` is a dictionary created everytime Python engine starts, as such, it is cleared when the engine is reset.

All settings are stored in a dictionary with a *name*. This is to organise the settings per script and prevent overlapping settings from different scripts.

This is useful for storing the user's previously entered values or as toggle switching a function.

Set value to Sticky
-------------------

Values can be set to sticky by calling the :py:func:`StickySet` function.


Get value from Sticky
---------------------

Stored values can be retrieved from sticky by calling the :py:func:`StickyGet` function.

Example
-------

.. literalinclude:: ./scriptcontextSticky.py
    :linenos:
    :language: python



.. note::
    If you can not think of a name, the built-in ``__file__`` variable can be used as a name input, this is the absolute file path of the current script
