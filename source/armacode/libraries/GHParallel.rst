GHParallel
----------

.. py:Function:: GHParallel(method, driverInputTree, *args, **kwargs)


Allows a Grasshopper component to process each branch with parallel processing. Principal input must have DataTree Access.

:param driverInputTree: Primary input Tree to process.
:param Additional inputs can be added. This can be Tree, list, or individual item. If Tree, it must have same amount of branches.:

Kwargs:
    multiOutput: Set this to True if the method return multiple values. Default to False
    If False, the output will be a single data Tree.
    If True, this will return a list of DataTree per output.

.. rubric:: Example

# Set up a component in Grasshopper with Inputs 'B', 'P' having Tree Access.
import Rhino
import armacode
import scriptcontext

def BrepPlane(plane, brep):
    global tolerance
    rc = Rhino.Geometry.Intersect.Intersection.BrepPlane(brep, plane, tolerance)
    return rc

tolerance = scriptcontext.doc.ModelAbsoluteTolerance
rc = armacode.GHParallel(BrepPlane, P, B, multiOutput=True)
G = rc[1]
