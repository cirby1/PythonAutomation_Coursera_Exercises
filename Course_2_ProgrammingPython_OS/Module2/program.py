"""
#1. The create_python_script function creates a new python script in the current working directory, adds the line of comments to it declared by the comments variable, and returns the size of the new file. Fill in the gaps to create a script called, "Program.py".  

def create_python_script(filename):
    comments = "#Start of a new Python Program."
    with ___:
        filesize = ___
    return(filesize)

print(create_python_script("program.py"))
"""

#Okay so how would I create a new python script in the current working directory? Probably with the open command?

with open("N64Wishlist", "w") as wishlist:
    wishlist.write("stuff") 
