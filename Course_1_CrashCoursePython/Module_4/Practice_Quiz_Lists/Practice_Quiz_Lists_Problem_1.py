#1 Fill in the blank using a for loop. With the given list of "filenames", this code should rename all files with the extension .hpp to the extension .h. The code should then generate a new list called "new_filenames" that contains the file names with the new extension. 

#You are given a list of filenames like this:
#filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]

#Output the list with all of the ".hpp" files renamed to end with ".h". Leave the other filenames along. For this question, you must use a for loop to create the list. 

#This program is wrong because it messed with all the other file types. I need to change it to where it only changes .hpp.


"""
def changefilenames():
    filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
    #Generate new_filenames as a list containing the new filenames using as many lines of code as your chosen method requires.

    #I guess I will check for all the different extensions and change them out.
    new_filenames = []
    for filename in filenames:
        if filename.endswith(".hpp"):
            newfilename = filename.split(".hpp")
            newfilename = newfilename[0] + ".h"
            new_filenames.append(newfilename)
        elif filename.endswith(".c"):
            newfilename = filename.split(".c")
            newfilename = newfilename[0] + ".h"
            new_filenames.append(newfilename)
        elif filename.endswith(".out"):
            newfilename = filename.split(".out")
            newfilename = newfilename[0] + ".h"
            new_filenames.append(newfilename)
        else:
            return new_filenames
    return new_filenames
"""

print(changefilenames())


