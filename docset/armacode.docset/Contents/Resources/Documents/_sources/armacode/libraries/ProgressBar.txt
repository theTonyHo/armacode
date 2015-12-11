ProgressBar
-----------

.. py:Function:: ProgressBar(value, lower, upper, label='', embed_label=True, show_percent=True, allowEscape=1)


Display the progress of the script using the built-in Progress Meter in Status Bar.
Automatically show and hide meter at start and end.
:param label = short description of the progesss:
:param value = current value of the progress bar to display:
:param lower = lower limit of the progress meter's range:
:param upper = upper limit of the progress meter's range:
:param embed_label[opt] = if True, the label will show inside the meter.:
                                                                          If false, the label will show to the left of the meter
:param show_percent[opt] = show the percent complete:

:returns: Previous value on success