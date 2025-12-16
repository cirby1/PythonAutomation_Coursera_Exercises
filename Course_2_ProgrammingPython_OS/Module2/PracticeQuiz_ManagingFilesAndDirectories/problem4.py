#4 - The file_date function creates a new file in the current working directory, checks the date that the file was modified, and returns just the date portion of the timestamp in the format yyyy-mm-dd. Fill in the gaps to create a file called "newfile.txt" and check the date that it was modified. 

import os
import datetime

def file_date(filename):
    #Create the file in the current directory.
    with open(filename, "w"):
        pass

    timestamp = os.path.getmtime(filename)
    newtimestamp = datetime.datetime.fromtimestamp(timestamp) 
    newtimestamp = str(newtimestamp)
    newtimestamp = (newtimestamp[0:11])
    #Return just the date portion.
    #Hint: how many characters are in "yyyy-mm-dd". 
    return("{}".format(newtimestamp))

print(file_date("newfile.txt"))
