#Here we are importing the csv python tools. They are similar to just reading/writing files I believe.
import csv

#Make a shortcut name so it's easier to write Python and use the typical open function and just plug in the name of the csv file that has all the values. It's going to look like garbly gook with a bunch of commas in between. 
f = open("csv_file.txt")

#Here we go ahead and open the entire file by using the reader function. 
csv_f = csv.reader(f)

#Cycle through each row in the spreadsheet.
for row in csv_f:
    name, phone, role = row #Here we are doing a trick where we assign a temple tuple of variables to a variable on the right. So the first value in the list is gonna be the name, the second the phone, and the third the role. 
    #Then remember the format function will print out the information in the CSV as a nice looking document going down. And we just specify what information is on each line.
    print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))

f.close()
