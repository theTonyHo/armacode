.. index:: DocumentManager (Command)

.. _documentmanager_cmd:

DocumentManager
---------------
Document Manager
Features:
    Read Object Properties to Excel
    Read Layout Properties to Excel
    Manipulate and Update Objects and Layout from Excel File

Document Manager can be used in the following scenarios:

1. The user can use the RDM workbook to quickly manipulate the properties of the Rhino document. (Non-Associated Link)
2. The user can use the RDM to manage quanity of objects and also drawing register.(Associated Link)

Read from Rhino document to Excel file.
Save the workbook to the temporary folder.

If the user wants to maintain the association between the workbook and the Rhino document,
the workbook needs to be saved to a more permanent location, preferrably
the same folder as the Rhino document:

For Example:

    Model_3D.3dm
    Model_3D_RDM.xlsx

Working with unassociated workbooks, best practice is to close the Rhino Document Manager workbook after update

RDM Open the workbook in this order, :

    Associated workbook
    Active workbook with title "Rhino Document Manager"
    armacode Excel Template.

Association link will only be created on Update.
Association link will NOT be created if the Excel file is located in the temporary folder

Usage:
Rhino to Excel:
Perform Read Operation to a new RDM From Template.
Format the column to General or Number as required and convert them to numbers.
Subsequent Read operations will retain formatting.

Excel to Rhino:
General and Numbers update as RAW Values.
For example, cell has value of 3.14259 is formatted as 3.14, the updated UserText is 3.14259
To force a column to be Update as Text, apply Text formatting BEFORE enter/paste values. If pasted, paste Values Only.
This is to ensure that what you see is what you get. For example numbers with padding i.e. 001.

Calulations and Manipulation:
Create non-UserText columns to help with calculations and manipulation.
These data will remain on Read/Update operations.
It is best for Dates Time and other complex data types.
Use these columns in a pivot table.

Recommended PivotTable schedules:
Best is to have one RDM per Rhino Model.
Always create a new RDM to manipulate data for Work In Progress.
Once data is verified and checked, read to the associated RDM which is used to produce pivot tables schedules

Depending on the size and complexity of project, There are two ways to manage Rhino Model and RDMs:
* One Model for Sub Framing structure (One material per sheet in RDM)
* One Model for Facade (One type per sheet in RDM)


Update:
    21/10/2014:
        Command Line Interface.
        Option to maintain table columns. Useful for retaining the formulas.
    22/10/2014:
        Command Line Interface. Fix Excel Opening before prompt finishes.
        Update Tables to auto fit after read operation.
    04/05/2016:
        Selection GUI to select from active Workbooks to read to or update from.
    12/05/2017:
        Read operations improvement. Data reshuffled to match Table Headers and populate in the correct column
        All data should come in as Text only. This is for compatibility in the Update operation to avoid surprises.
        All custom columns should be on the end, right side, of the table
    09/04/2018:
        Added new Excel Table method called ColumnFormat, allowing retrieving and modifying number format per column.
        Data in Read operations treated as TEXT on first run.
        User modify RDM with appropriate number format to suit.
        Number format is maintained on subsequent Read operations.
        Added processDates switch to convert manipulate Date values.
    15/05/2018:
        Match Layout Read/Update routine with Objects Read/Update
        Layout Mode force Text format.
