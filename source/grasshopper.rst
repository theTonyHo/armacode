.. contents::

Introduction
============

>Grasshopper Definition Library

Definitions
===========

>Definitions are workflows which perform a sequence of processes.

Definitions are often experimental and are still in development.

All processes inside the definition should be documented thoroughly

Project specific definitions are placed in the Project's Code folder.

Definitions can be converted into a `User Object` and should be placed in "`Workflow` panel.

User Objects
============
>User objects are custom components, may containing a cluster of components, that are saved with user customisation for easy access.

User objects are placed on the tab of the Grasshopper interface when created.
User objects can be organised in `panels` under the user defined tab.

Clusters
--------

>Cluster is a component containing a group of connected components which perform a specific routine definition.

    Inputs -> Components -> Outputs

__Preview Content__

Components that are __Preview Enabled__ will be visible if the cluster is __Preview Enabled__.

Component with special visual preview such as `Text Tag` or `Custom Preview` that is inside of a cluster can be previewed. They are off by default. Turn this on by right clicking the component and select `Preview Content`.


Authoring
---------

All User Objects created from Clusters autofill information from the Author settings in the Grasshopper Preference panel.

    File -> Preference - > Author




GHPython User Object
====================

>GHPython allows user to access Python libraries as well as implement any of the available Grasshopper components through Python scripting.

Script Context
--------------

The Python script can be executed in multiple scope of context. 

### ghdoc

As default, ghpython runs in the ghdoc context 
Geometries created using rhinoscriptsyntax are stored in the ghdoc.

### Rhino

Run the python script in standard/native Rhino context.
Geometries created using rhinoscriptsynctax are added to the Rhino document when executed.
This context is useful to access collections of Objects, Layers and Groups within the active document.
Set the python script context to the active Rhino document by including the following:


    import Rhino
    import scriptcontext

    scriptcontext.doc = Rhino.RhinoDoc.ActiveDoc

Data Access
-----------

>Data Access determines the way script variables are defined from input Parameters

### Item Access

The script is executed __once per item__ in the data tree. The component will treat input parameters with mis-matched item count using Longest List.
Input variable is defined as an __object__


### List Access

The script is executed __once per branch__ in the data tree. The component will treat input parameters with mis-matched branch count using Longest List.
Input variable is defined as a __list__ object


### Tree Access

The script is executed __once__.
Input variable is defined as a __Grasshopper.DataTree__ object.

DataTree object contains branch and path information. It is for advanced users to maintain relationship between the data accross branches.

Parameters
----------

### Arguments

>Input Parameters

Input Parameters can be added as required.

Each argument needs to be defined of a data structure and data type in the Grasshopper document using the interface.

Each argument can be defined with default value


### Returns

>Output Parameters

Output Parameters can be added as required.

Each return is defined in the Python script.
Return is often an object or a list of objects. 
For nested lists, consider constructing a DataTree structure.


Docstring
---------
>Docstring for GHPython component is useful for user to understand the component.

    Title
    Description
        Args
            input: input description
        Returns
            output: output description
        Help
            remarks content
        **TODO and Additional Sections


__Title__

First line of the docstring should be the full name of the component. Note that this does not define the Nickname nor the Full name of the component.
This is included in the _Tooltip_ of the component

__Description__

This is included in the _Tooltip_ of the component
This content will be visible under the __Help__ section.

__Args__

Each line defines the _Tooltip_ of an Input parameter
This content will be visible as "Input Parameters" under the __Help__ section.

__Returns__

Each line defines the _Tooltip_ of an Output parameter.
This content will be visible as "Output Parameters" under the __Help__ section.

__Help__

This content will be visible as _Remarks_ under the __Help__ section.


### Example

    """
    Arithmetic Series
    Computes the Sum of an Arithmetic Progression, or the
    sum of all numbers from F to L, included.
        Args:
            F: the first number included in the series.
            L: the last number included in the series.
        Returns:
            S: If F > L, then sum of all numbers [F,L].
                If F = L, then 0.
                If F < L, then sum of all numbers (L,F).
            K: Not used.
        Help:
            See also the Gauss elementary school story:
            http://mathworld.wolfram.com/ArithmeticSeries.html
        Note: Any content here is also included in the Help section.
    """

Refer to [GHPython DocUtil] for more information


Advanced
========

Node-in-code
------------

Refer to Steve Baer post about [Node-in-code] with new ghPython component

Multi-threading
---------------

GHPython library has a method to utilise Multi-threading technology. Refer to Steve Baer post about multi-threading in [Node-in-code]

Outside the canvas
------------------

GHPython can be used ouside of the Grasshopper canvas interface. Refer to Steve Baer post about [GHPython Outside-the-canvas]

Reference
=========

[GHPython Github](https://github.com/mcneel/ghpython)


[GHPython DocUtil]:https://github.com/mcneel/ghpython/blob/master/Component/DocStringUtils.cs
[Node-in-code]:http://stevebaer.wordpress.com/2013/12/11/ghpython-node-in-code/
[GHPython Outside-the-canvas]:http://stevebaer.wordpress.com/2013/12/12/ghpython-outside-the-canvas/
