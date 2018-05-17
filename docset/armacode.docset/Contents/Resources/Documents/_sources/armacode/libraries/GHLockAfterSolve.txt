GHLockAfterSolve
----------------

.. py:Function:: GHLockAfterSolve(ghPythonComponent, activate, message='Solution Solved')


Lock the GHPython component after solve to prevent further looping.

:param ghPythonComponent: The component to apply Lock state to. use "ghenv.Component" to reference itself.
:param activate: Activate Locking after solving this with the activate trigger input

.. rubric:: Example

import armacode
armacode.GHLockAfterSolve(ghenv.Component, activate )
