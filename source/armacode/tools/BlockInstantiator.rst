.. index:: BlockInstantiator (Tool)

.. _tools.blockinstantiator:

BlockInstantiator
-----------------
Instantiate Block

Block instance can be placed by specifying target planes.

Target plane is determined based on different input object.

Point Object will use the current CPlane with origin at the Point coordinates.
Surface Object will use the Evaluated Frame at normal parameters (0.5,0.5)
Polyline Object (two segment/3Pts Polyline) where points correspond to (X,O,Y). Plane is aligned to the direction of the last segment.
Text Object. Base Plane of the text object is used.