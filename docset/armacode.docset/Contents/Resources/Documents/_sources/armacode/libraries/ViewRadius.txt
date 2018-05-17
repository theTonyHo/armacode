ViewRadius
----------

.. py:Function:: ViewRadius(view=None, radius=None)


Returns or sets the radius of a parallel-projected view. Useful
when you need an absolute zoom factor for a parallel-projected view
:param view: [opt] title or id of the view. If omitted, current active view is used
:param radius: [opt] the view radius

:returns: if radius is not specified, the current view radius for the specified view
          if radius is specified, the previous view radius for the specified view
