.. index:: MinBB2D (Command)

.. _minbb2d_cmd:

MinBB2D
-------
Minimum Bounding Box (Area Binary Search).
Computes the minimum area bounding box of a flat curve using binary search.
a.linares @ AR-MA 2017

    Args:
        CRV : Curve to calculate the bounding box of.
        T : Minimum area differential between calculations used for convergence.
        n: Maximun number of iterations allowed

    Returns:
        Box : The calculated bounding box