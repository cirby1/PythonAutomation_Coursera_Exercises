#1- Create Python Script function creates a new Python script in the current working directory, adds the line of comments to it declared by the comments variable, and returns the file size of the file. Fill in the gaps to create a script called "program.py". 
import os

def create_python_script(filename):
    comments = "# Start of a new Python program"
    with open(filename, "w") as file:
        file.write(comments)
    filesize = os.path.getsize(filename)
    return filesize

print(create_python_script("program.py"))
