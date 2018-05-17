TextObjectTextFormula
---------------------

.. py:Function:: TextObjectTextFormula(object_id, textFormula=None)


Returns or modifies the text string of a text object.
:param object_id = the identifier of a text object:
:param text [opt] = a new text string:

:returns: if text is not specified, the current string value if successful
          if text is specified, the previous string value if successful
          None if not successful, or on error
