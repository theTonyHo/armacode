PYTHON
======

>Python script library mainly for Rhinoceros 5

Docstring
---------

> Following a consistent docstring format is recommended for other users to understand more about the code.

Refer to the [Google Code style guide](http://google-styleguide.googlecode.com/svn/trunk/pyguide.html#Comments) for more documentation

Refer to the [Sphinx compatible examples](http://sphinx-doc.org/latest/ext/example_google.html)

    Title
    Description
    Args:
        input: input description
    Returns:
        output: output description
    Help:
        remarks content
    **TODO and Additional Sections

### Example

Method Docstring:

    def fetch_bigtable_rows(big_table, keys, other_silly_variable=None):
        """Fetches rows from a Bigtable.

        Retrieves rows pertaining to the given keys from the Table instance
        represented by big_table.  Silly things may happen if
        other_silly_variable is not None.

        Args:
            big_table: An open Bigtable Table instance.
            keys: A sequence of strings representing the key of each table row
                to fetch.
            other_silly_variable: Another optional variable, that has a much
                longer name than the other args, and which does nothing.

        Returns:
            A dict mapping keys to the corresponding table row data
            fetched. Each row is represented as a tuple of strings. For
            example:

            {'Serak': ('Rigel VII', 'Preparer'),
             'Zim': ('Irk', 'Invader'),
             'Lrrr': ('Omicron Persei 8', 'Emperor')}

            If a key from the keys argument is missing from the dictionary,
            then that row was not found in the table.

        Raises:
            IOError: An error occurred accessing the bigtable.Table object.
        """
        pass


Class Docstring:

    class SampleClass(object):
        """Summary of class here.

        Longer class information....
        Longer class information....

        Attributes:
            likes_spam: A boolean indicating if we like SPAM or not.
            eggs: An integer count of the eggs we have laid.
        """

        def __init__(self, likes_spam=False):
            """Inits SampleClass with blah."""
            self.likes_spam = likes_spam
            self.eggs = 0

        def public_method(self):
            """Performs operation blah."""

Folder structure
================

The folder structure for armacode should be organised following the following structure:

	\classes
		__init__.py
		\ClassBaseOne
			__init__.py
			ClassOne.py
		\ClassBaseTwo
			__init__.py
			ClassTwo.py
		\ClassBaseThree
			__init__.py
			ClassThree.py
	\libraries
		__init__.py
		ModuleOne.py
		ModuleTwo.py
		ModuleThree.py
	\tools
		__init__.py
		toolOne.py
		toolTwo.py
		toolThree.py
	armacode.py
	config-default.py
	config-user.py



Classes
=======

>Classes are predefined objects which can be used in future projects for Research, and possibly Production, purposes.

Each class should be in their own ClassBase folder. For example, Particle, MovingParticle, FlockingParticle would be part of the ParticleSystem Class.

Access the classes with the following:

	import armacode
	p = armacode.classes.Particle()


Libraries
=========

>Library of all the useful methods which can be used during the development of a script or a workflow sequence. Each of the method should Only perform one small single purpose. For example:

	Add(x,y):
		result = x + y
		return result
	
	Average(x,y):
		result = Add(x,y) / 2 
		return result
	Note: Average function reuses Add function to reduce data redundancy and help code management.

Access the method with the following:

	import armacode
	line = armacode.AddLine()


Tools
=====

>Tools are workflow-based scripts which represent a sequence of steps to produce a desired output. This usually involve interactive user inputs where decisions need to be made 

Access the tool with the following:

	import armacode
	line = armacode.tools.AddNameTags()

