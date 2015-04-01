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
    
    TODO and Additional Sections (See Napoleon readthedocs)
    """

.. note :: 
    
    Docstring also applies to GHPython component, the docstring is used to assign tooltips for the component

    Help section appears on GHPython Help content.

.. rubric:: References:

* `Google Code style guide <http://google-styleguide.googlecode.com/svn/trunk/pyguide.html#Comments>`_ 

* `Sphinx compatible examples <http://sphinx-doc.org/latest/ext/example_google.html>`_

* `Napoleon Google Docstrings <http://sphinxcontrib-napoleon.readthedocs.org/en/latest/#docstring-sections>`_


.. Folder structure
.. ================

.. The folder structure for armacode should be organised following the following structure

..         armacode/
..             __init__.py
..             classes/
..                     __init__.py
..                     ClassBaseOne/
..                             __init__.py
..                             ClassOne.py
..                     ClassBaseTwo/
..                             __init__.py
..                             ClassTwo.py
..                     ClassBaseThree/
..                             __init__.py
..                             ClassThree.py
..             libraries/
..                     __init__.py
..                     ModuleOne.py
..                     ModuleTwo.py
..                     ModuleThree.py
..             tools/
..                     __init__.py
..                     toolOne.py
..                     toolTwo.py
..                     toolThree.py



