.. index:: SetCurrentDimStyleToActiveViewport (Command)

.. _setcurrentdimstyletoactiveviewport_cmd:

SetCurrentDimStyleToActiveViewport
----------------------------------
Set dimension style as current. DimStyle is chosen according to the scale of the detail viewport.

In Model: Prompt user to select DimStyle.
In Layout: Set DimStyle to 1:1.
In Detail: Set the DimStyle based on Viewport scale, for example 1:25.

If a DimStyle is not available, prompt user to select a DimStyle. Suppress prompt in scripted mode (-)