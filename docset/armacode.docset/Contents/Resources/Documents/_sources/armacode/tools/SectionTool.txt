.. index:: SectionTool (Tool)

.. _tools.sectiontool:

SectionTool
-----------
Section Tool
Generate section views in Rhino.
Each section view is stored as a block definition.
Section view is created from a surface. Plane of the surface is crucial. Section is limited to the inverse of the plane's Z Axis, i.e. looking through.
User is able to update the section views by clickin on the existing section instance.
User can update the bounds of the section by clicking on the surface or the section view block.

//Update 2016-03-31:
    Update User Interface. When Base point is default to point evaluated at 0.5,0.5 of the plane. Depth is default to 0.0, to make a section.
    Optimized by skipping make2D if depth is 0.0, only make section lines.

//Update 2016-04-01:
    Smart section now works with objects inside block instances.