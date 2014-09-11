import armacode
import rhinoscriptsyntax as rs

def main():
    response = armacode.StickyGet("stickyExample", "userName")
    if not response:
        response = rs.StringBox("Hello, what is your name ?", response, "Please enter Your name")
    else:
        rs.MessageBox("Welcome back {} !".format(response), 0, "Message")
    
    armacode.StickySet("stickyExample", userName=response)

if __name__ == "__main__":
    main()