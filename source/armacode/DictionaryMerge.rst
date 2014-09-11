DictionaryMerge
---------------

.. py:Function:: DictionaryMerge(dictA, dictB, overwrite=True)


Merge two dictionaries into one.

:param dictA: dictionary object
:param dictB: dictionary object to merge with.
:param overwrite: If True, the values in dictB will replace the value in dictA if the same key is found.


:returns: The merged dictionary on success.

.. rubric:: Example

a = {"a":1, "b":4}
b = {"b":1, "c":16}
z = DictionaryCombine(a, b)
print z
>>>>{'a': 1, 'c': 16, 'b': 1}
