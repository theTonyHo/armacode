ARMAcode
========

|docs|

armaCode Documentation Repository. 
Note that this is not the actual code repository

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

Install the following in order:

- doc2dash - ``pip install doc2dash==2.1.0``.
- Sphinx (1.3.5 installed with doc2dash)
- Sphinxcontrib-napoleon - ``pip install sphinxcontrib-napoleon``

**Notes:**

**doc2dash** requires specific version of dependencies. Only dedicate this configuration/computer to build armacode to avoid conflict with other projects.

Regarding compatibility between Sphinx and napoleon version dependency as described on the official website, Sphinx and napoleon will be working independently. Napoleon is used inside DocGenerator to convert Google docstring. Sphinx is to build the generated rst.

The required cusomized version of sphinxcontrib-napoleon is already included in this repository. Installing it, will install all of its required dependencies.

Theme customized and adapted from Sphinx Bootstrap Theme https://github.com/ryan-roemer/sphinx-bootstrap-theme . Modify in the following folder ``.\theme\bootstrap\static\bootswatch-3.2.0\ar-ma``


Instructions
------------

All documentation is generated from armacode repository. The Version of the repository is synchronised automatically when documentation is generated.

#. Run ``docGenerator.py`` in RhinoPython to generate the **current** documentation source files from the armacode module
#. Run ``make-html-and-test.bat`` to generate HTML files
#. Run ``make-htmlhelp.bat`` to generate HTMLHELP file
#. Run ``make-docset-from-html.bat`` to generate docset for Zeal/Dash
#. Run ``make-docset-tgz.bat`` to create tgz file (package for Zeal/Docset)
#. Run ``git-publish.sh`` to automatically publish the generated content. This script automatically synchronize the version of armacode module.

Code Update
-----------

It is very important to keep the documentation repository up to date.

Every time armacode has been updated, in master branch only, execute the above instructions immediately to regenerate the documentation.

All documentation should reflect on the master/production branch where everyone has access to, both developers and end users.
