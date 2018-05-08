
.. toctree::
   :maxdepth: 2
   index.rst

ARMAcode
========

|docs|

armaCode Documentation Repository. Note that this is not the actual code repository

Documentation
-------------

ReadTheDocs: http://armacode.readthedocs.org/

Zeal/Dash Docset feed: https://raw.githubusercontent.com/theTonyHo/armacode/master/feed/armacode.xml

.. |docs| image:: http://readthedocs.org/projects/armacode/badge/
    :alt: Documentation Status
    :scale: 100%
    :target: http://armacode.readthedocs.org/

Dependencies
------------

*. doc2dash - ``pip install doc2dash==2.1.0``
*. Sphinx (1.3.5 installed with doc2dash)
*. Sphinxcontrib-napoleon - ``pip install sphinxcontrib-napoleon``

..notes::Notes:

- doc2dash dequires specific version of dependencies. Only dedicate this configuration/computer to build armacode to avoid conflict with other projects.

- Regarding compatibility between Sphinx and napoleon version dependency as described on the official website, Sphinx and napoleon will be working independently. Napoleon is used inside DocGenerator to convert Google docstring. Sphinx is to build the generated rst.

- The required cusomized version of sphinxcontrib-napoleon is already included in this repository.

- Theme customized and adapted from Sphinx Bootstrap Theme https://github.com/ryan-roemer/sphinx-bootstrap-theme . Modify in the following folder ``.\theme\bootstrap\static\bootswatch-3.2.0\ar-ma``


Instructions
------------

All documentation is generated from armacode repository. The Version of the repository is synchronised automatically when documentation is generated.

#. Run ``docGenerator.py`` in RhinoPython to generate the **current** documentation source files from the armacode module
#. Run ``make-html-and-test.bat`` to generate HTML files
#. Run ``make-htmlhelp.bat`` to generate HTMLHELP file
#. Run ``make-docset-from-html.bat`` to generate docset for Zeal/Dash
#. Run ``make-docset-tgz.bat`` to create tgz file (package for Zeal/Docset)
#. Run ``git-publish.sh`` to automatically publish the generated content. This script automatically synchronize the version of armacode module.

Version Tagging - Superseded 
---------------
The instruction below is superseded. Refer to instructions within armacode repository regarding version tagging and incrementation.

This will guide you to increment a new version for armacode repository.

#. Modify the ``VERSION`` file to the new version i.e. "v.1.1.4". If pre-commit hook is active, it will auto correct the remaining of the file on commit. Otherwise, modify accordingly.
#. Commit the modification
#. Push and Merge into Master branch
#. Add the version tag in the local repository
#. Push the tags to the remote repository

