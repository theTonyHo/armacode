CSVWrite
--------

.. py:Function:: CSVWrite(fileName, data, dialect=None, fieldnames=None)


Write data into a new CSV File.
The data needs to be formated as a list of dictionaries.
The keys will be the column name.
Each dictionary represent a row of data

**Require csv module from IronPython 2.7.4