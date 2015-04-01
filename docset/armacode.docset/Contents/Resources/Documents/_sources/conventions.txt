.. A few words

Conventions
===========

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