.. A few words

Conventions
===========

Docstring
---------


    Following a consistent docstring format is recommended for other users to understand more about the code.

.. rubric:: Google Docstring:

::

    """
    Title
    Description

    Args:
        input (type) : input description
    
    Returns:
        output (type) : output description
    
    References:
        Some source or reference links.

    Help:
        remarks content
    
    TODO and Additional Sections (See Napoleon readthedocs)
    """

.. note :: 
    
    Docstring also applies to GHPython component, the docstring is used to assign tooltips for the component

    Help section appears on GHPython Help content.

.. rubric:: References:

* `Google Code style guide <http://google-styleguide.googlecode.com/svn/trunk/pyguide.html#Comments>`_ 

* `Sphinx compatible examples <http://sphinx-doc.org/latest/ext/example_google.html>`_

* `Napoleon Google Docstrings <http://sphinxcontrib-napoleon.readthedocs.org/en/latest/#docstring-sections>`_


Workflow
--------

    Workflow script is a sequence of operations which process a predefined Input and generate a specific result Output.

All generic workflow scripts should be placed in ``Tools``.

All project specific scripts should be placed in their corresponding ``Code`` folder per project.


.. rubric :: Template:

.. literalinclude:: ./examples/WorkflowTemplate.py
    :linenos:
    :language: python

.. note ::
    All workflow should be defined in a ``main()`` function and call it safely using ``if __name__ == "__main__":``


Command
-------

    A python script can be used as a Rhino Command.

Workflow that are stable has been fully tested and working as intended should be turned into a command for easy execution.

Command python files are named with a suffix ``_cmd.py``. All commands are stored in the ``Plug-in`` folder. 

**Create a command**:

* Open   Python script editor using ``EditPythonScript``
* File > New > Command
* Select the AR-MA plugin.


.. literalinclude:: ./examples/Command_cmd.py
    :linenos:
    :language: python