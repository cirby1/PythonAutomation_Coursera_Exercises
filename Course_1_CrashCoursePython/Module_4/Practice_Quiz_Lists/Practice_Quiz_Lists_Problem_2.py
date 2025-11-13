#Fill in the blank using a list comprehension. With the given list of "filenames", this code should rename all files with the extension .hpp to the extension .h. The code function should then generate a new list called "new_filenames" that contains the filenames with the new extension.

#You are given a list of filenames like this:
#filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
#Generate new_filenames as a list containing the new filenames using as many lines of code as your chosen method requires.

def changefilenamestoh(input_filenamelist):
    result_list = []
    for individual_filename in input_filenamelist:
        if individual_filename.endswith(".hpp"):
            split_word = individual_filename.split(".hpp")
            #print(split_word)
            newfilename = split_word[0] + ".h"
            result_list.append(newfilename)
        else:
            result_list.append(individual_filename)
    return result_list

print(changefilenamestoh(filenames))

#The list comprehension way that I came up with was:
#new_filenames = [individual_file[:-4] + ".h" if individual_file[-4:] == ".hpp" else individual_file for individual_file in filenames]
           





changefilenamestoh(filenames)
    
    
















#Should print out ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

