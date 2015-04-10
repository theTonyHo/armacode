import Rhino
import armacode
import rhinoscriptsyntax as rs

def Hello():
    print "HELLO"
    return

def main():
    
    # Configure options and place in a dictionary.
    # Set the key as a string, this will be used as the option Name.
    # Note that the option Name can not contain any space
    options = {}
    options["Toggle"] = Rhino.Input.Custom.OptionToggle(True, "No", "Yes")
    options["Float"] = Rhino.Input.Custom.OptionDouble(0.01)
    options["Integer"] = Rhino.Input.Custom.OptionInteger(5)
    options["Color"] = Rhino.Input.Custom.OptionColor(rs.coercecolor((255,0,0), False))
    options["Operation"] = Hello
    options["String"] = None
    options["String2"] = "Proper String Value"
    options["List"] = ["A","B","C"]
    
    object_ids = armacode.GetObjectsWithOptions(custom_options=options)
    print "Selected GUIDs : {}".format(object_ids)
    
    if object_ids:
        for name in options:
            print "{} : {}".format(name, options[name])
    

if __name__ == "__main__":
    main()