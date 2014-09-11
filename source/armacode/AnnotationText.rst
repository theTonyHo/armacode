AnnotationText
--------------

.. py:method:: AnnotationText(object_id, usertext=None)


Returns of modifies the user text string of a dimension object.
The usertext is the string that gets printed when the dimension is defined.
If the provided usertext is the same as the display text. Nothing will





:returns: False if usertext is provided but unchanged. If usertext is not specified, the current usertext string. If usertext is specified, the previous usertext string.

.. rubric:: Notes

Comparing the new user text to the current display text is critical. This is to prevent the user from replacing a formula with a static text which has the same display value.

.. rubric:: References

Extended from rs.DimensionUserText()
