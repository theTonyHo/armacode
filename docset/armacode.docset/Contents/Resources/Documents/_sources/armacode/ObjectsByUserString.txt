ObjectsByUserString
-------------------

.. py:function:: ObjectsByUserString(key, value='*', caseSensitive=True)


Finds all objects whose UserString matches the search patterns.

:param key: Search pattern for UserString keys (supported wildcards are: ? = any single
            character, * = any sequence of characters).

:param value: Search pattern for UserString values (supported wildcards are: ? = any single
              character, * = any sequence of characters).

:param caseSensitive: If true, string comparison will be case sensitive.


:returns: An array of all objects whose UserString matches with the search patterns or
          null when no such objects could be found.