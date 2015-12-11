
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


Instructions
------------

All documentation is generated from armacode repository. The Version of the repository is synchronised automatically when documentation is generated.

#. Run ``docGenerator.py`` in RhinoPython to generate the **current** documentation source files from the armacode module
#. Run ``make-html-and-test.bat`` to generate HTML files
#. Run ``make-htmlhelp.bat`` to generate HTMLHELP file
#. Run ``make-docset-from-html.bat`` to generate docset for Zeal/Dash
#. Run ``make-docset-tgz.bat`` to create tgz file (package for Zeal/Docset)
#. Run ``git-publish.sh`` to automatically publish the generated content.

Version Tagging
---------------

This will guide you to increment a new version for armacode repository.

#. Modify the ``VERSION`` file to the new version i.e. "v.1.1.4". If pre-commit hook is active, it will auto correct the remaining of the file on commit. Otherwise, modify accordingly.
#. Commit the modification
#. Push and Merge into Master branch
#. Add the version tag in the local repository
#. Push the tags to the remote repository

