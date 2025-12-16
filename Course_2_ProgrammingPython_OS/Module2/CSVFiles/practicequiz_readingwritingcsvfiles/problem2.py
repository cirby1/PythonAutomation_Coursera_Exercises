#1 We're working ona  list of flowers and adding info about each one.

#The create function writes this information to a csv file. 

#The contents_of_file function reads this file into records and returns a nicely formatted block.

#Fill in the gaps of the contents of the contents_of_files function to turn the data into the CSV file into a dictionary using DictReader.


import os
import csv

#Create file with data in it.

def create_file(filename):
    with open(filename, "w") as file:
        file.write("name,color,type\n")
        file.write("carnation,pink,annual\n")
        file.write("daffodil,yellow,perennial\n")
        file.write("iris,blue,perennial\n")
        file.write("poinsetta,red,perennial\n")
        file.write("sunflower,yellow,annual\n")

#Read the file contents and format the information about each row.
def contents_of_file(filename):
    return_string = ""
    
    #Call the function to create the file.
    create_file(filename)

    #Open the file.
    with open(filename) as flowers:
        next(flowers)
        #Read the rows of the file into a dictionary.
        rows = csv.reader(flowers)
        #Process each item in the dictionary.
        for row in rows:
            name, color, type = row 
            #Format the return string for data rows only.
            return_string += "a {} {} is {}\n".format(color,name,type)

    return return_string




print(contents_of_file("flowers.csv"))


#Excellent! I was able to do this! And it worked splendidly!!!!









