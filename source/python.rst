Python
======


.. toctree::
   :maxdepth: 5


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
    
    **TODO and Additional Sections
    """

.. note :: 
    
    Docstring also applies to GHPython component, the docstring is used to assign tooltips for the component

    Help section appears on GHPython Help content.

.. rubric:: References:

* `Google Code style guide <http://google-styleguide.googlecode.com/svn/trunk/pyguide.html#Comments>`_ 

* `Sphinx compatible examples <http://sphinx-doc.org/latest/ext/example_google.html>`_

* `Napoleon Google Docstrings Example <http://sphinxcontrib-napoleon.readthedocs.org/en/latest/example_google.html>`_

Folder structure
================

The folder structure for armacode should be organised following the following structure::

        armacode/
            classes/
                    __init__.py
                    ClassBaseOne/
                            __init__.py
                            ClassOne.py
                    ClassBaseTwo/
                            __init__.py
                            ClassTwo.py
                    ClassBaseThree/
                            __init__.py
                            ClassThree.py
            libraries/
                    __init__.py
                    ModuleOne.py
                    ModuleTwo.py
                    ModuleThree.py
            tools/
                    __init__.py
                    toolOne.py
                    toolTwo.py
                    toolThree.py
            __init__.py



Classes
-------

    Classes are predefined objects which can be used in future projects for Research, and possibly Production, purposes.

Each class should be in their own ClassBase folder. For example, Particle, MovingParticle, FlockingParticle would be part of the ParticleSystem Class.

Access the classes with the following::

    import armacode
    p = armacode.classes.Particle()


Libraries
---------

    Library of all the useful methods which can be used during the development of a script or a workflow sequence. 

Each of the method should Only perform one small single purpose. For example::

    Add(x,y):
        result = x + y
        return result
    
    Average(x,y):
        result = Add(x,y) / 2 
        return result

.. Note:: Average function reuses Add function to reduce data redundancy and help code management.

Access the method with the following::

    import armacode
    line = armacode.AddLine()


Tools
-----

    Tools are workflow-based scripts which represent a sequence of steps to produce a desired output.

A workflow usually involve interactive user inputs where decisions need to be made during the execution of a script.

Access the tool with the following::

    import armacode
    line = armacode.tools.AddNameTags.main()

