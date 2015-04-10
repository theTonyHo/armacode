.. index:: ObjectsLengthAdjustment (Tool)

.. _tools.objectslengthadjustment:

ObjectsLengthAdjustment
-----------------------
Manipulate multiple geometries based on a reference line to different lines.
This is similar to the concept of scale1D, however, the geometries do NOT get distorted,
The grip points get translated/moved.

//INPUT
Geometries to work on
Reference Line
Target Lines.

//PSEUDOCODE
Turn on grip Points for the geometries
Orient Reference line to the new line. Make a copy
Orient objects to the new line. Make a copy

With new geometries
Turn on grip points for all geometry
Get end points of reference line
Compare the GPs to the end points of the Line.
Get the closest end point to every GPs based on which end it is closest to.

Get translation vector from Reference End point to new End point.
Apply translation transformation.


//OUTPUT
Copied and transformed Geometries.