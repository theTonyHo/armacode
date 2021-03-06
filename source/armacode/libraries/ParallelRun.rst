ParallelRun
-----------

.. py:Function:: ParallelRun(function, data_list, flatten_results=False)


For each item in data_list execute the input function. Execution is
done on as many threads as there are CPUs on the computer.
Note that for function with more than one parameter, a dictionary
can be used to provide keyword arguments.
:param function: function to execute for each item in the data_list
:param data_list: list, tuple, or other enumerable data structure.
:param flatten_list [opt]: if True, when results are lists of lists the
                           results are flattened into a single list of results. If this is True,
                           you cannot depend on the result list being the same size as the input list

:returns: list of results containing the return from each call to the input function
