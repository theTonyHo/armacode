ObjectsByUserString
-------------------
Finds all objects whose UserString matches the search patterns.

key: Search pattern for UserString keys (supported wildcards are: ? = any single
 character, * = any sequence of characters).

value: Search pattern for UserString values (supported wildcards are: ? = any single
 character, * = any sequence of characters).

caseSensitive: If true, string comparison will be case sensitive.
Returns: An array of all objects whose UserString matches with the search patterns or
 null when no such objects could be found.