.. A few words

Libraries
=========

    Library of all the useful methods which can be used during the development of a script or a workflow sequence. 

Each of the method should Only perform one small single purpose. For example::

    Add(x,y):
        result = x + y
        return result
    
    Average(x,y):
        result = Add(x,y) / 2 
        return result

.. Note:: Average function reuses Add function to reduce data redundancy and help code management.

Access the method with the following::

    import armacode
    line = armacode.AddLine()

.. toctree::
   :maxdepth: 2
   :glob:
   
   armacode/libraries/*


