#2. The new_directory function creates a new directory inside the current working directory, then creates a new empty file inside the new directory, and returns the list of files in that directory. Fill in the gaps to create a file "script.py" in the directory "PythonPrograms".

import os

print(os.getcwd())

print(os.path.isdir("actionmovies"))

print(os.path.isdir("dramamovies"))

os.chdir("actionmovies")

print(os.getcwd())

with open("myactionmovielist.py", "w") as actionmovies:
    actionmovies.write("James Bond")
    actionmovies.write("Indiana Jones")
    actionmovies.write("Avatar")

print(os.getcwd())


"""
import os

def new_directory(directory, filename):
    #Creates script.py inside of PythonPrograms. 

    #This checks If we are in the directory that we are supposed to be. If it is False, then we will need to go there.
    if os.path.isdir(directory) == False:
        #If the directory that we are supposed to be in doesn't exist, then we make it. 
        os.mkdir(directory)

    #Okay, now let's change to that directory. Because It's either exists or it didn't and just got created. Either way we need to make sure that we are in it.
    os.chdir(directory)

    with open(filename) as file:
        #Create an empty file inside of the new directory.
        pass
     
    return os.listdir(directory)
"""

#print(new_directory("PythonPrograms", "script.py"))
