.. index:: SurfacePerforationMap (Tool)

.. _tools.surfaceperforationmap:

SurfacePerforationMap
---------------------
Generate a Perforation Map for a surface/panel

Perforation pattern may contain holes/curves in various shape and sizes, rendering or displaying these may dramatically decreases performance of the computer.
For any perforation pattern, it is best to have them as curves in the model.
This script uses the necessary geometries to create a transparency map and apply to that panel surface.
Surface must be shrunk, as in the Domain of the surface should be within the bounding box of the surface itself.

The Tony HO | AR-MA
Release: April 2016

.. todo::

   Batch operation. Associate perforation geometries by UserText to match with the surface. Can be defaulted to Object Name.
   Polysurfaces mapping such as panels with returns. ApplyPlanarMapping seems like a good path.
