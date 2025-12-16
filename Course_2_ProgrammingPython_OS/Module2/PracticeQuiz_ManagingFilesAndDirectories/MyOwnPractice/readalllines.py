import os

#Okay, let's print all the lines in a file. Remember to just use the "with open("filename") as newfilename:" command.

with open("allbooks.txt") as fivebooks:
    for line in fivebooks:
        print(line)
