.. index:: BullzipPDFPrinter (Tool)

.. _tools.bullzippdfprinter:

BullzipPDFPrinter
-----------------
Bullzip PDF Printer.
Print selected layouts into single individual PDFs.

The Tony HO | AR-MA
Release: May 2013

Dependencies:
    Bullzip PDF Printer

Update:
    03/05/2013
    Added Page selection Settings and file name format are stored in memory until reset
Update:
    24/11/2013
    Using Text Objects as Fields to be used in the filename
Update:
    07/06/2014
    Fix switching to view in order to print.
    Refactoring code.

Update:
    19/09/2014
    Revert to legacy mode: switch to layout before print. Individual layout settings, (i.e. portrait and landscape orientation) are not used when running in silent mode.
    21/10/2014
    Refactoring code to command.
    Store file name format in the document as user text for future prints.
Update:
    24/06/2015
    Optimised performance.
    If file name format only require #PAGE_NAME, no need to process text objects on layout.
    Layout Properties are processed at the very beginning of the script.

Update:
    23/04/2018
    Fixed Rhinoceros 6.
    Attempted to optimize performance. using WaitForFile.
    WaitforFile is useful, however, using scriptcontext to react to users Escape key press is preferred.
    Bullzip writes a package of files into the TEMP folder containing the pdf and some postscript files. This folder gets deleted upon completion.
    The postscript process takes a long time, however, unable to find a way to optimise the speed of the print.
    Tried reading the status.ini file inside the TEMP folder.