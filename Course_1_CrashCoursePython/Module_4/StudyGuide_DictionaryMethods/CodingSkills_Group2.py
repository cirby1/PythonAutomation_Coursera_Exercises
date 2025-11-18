#Skills Group 2

"""
This function contains a dictionary that basically has employee's full names. Their first name and last names. But it's organized with last names as the keys and a list of first names as the values. That way, if there's multiple people with "Garcia" for example, the values would have a list of all the people that have Garcia as their last name. 

You need to create a way to turn this dictionary into a list that has everyone's full name. A full name of First name and Last name together. The list should have everyone's names in first/last name format. 
"""

"""
The exercise says concatenate a value, string, and a key for each item in teh dictionary and append it to the end of the new list[] using the list.append(x) method.

Iterate over keys with multiple values from a dictionary using nested for loops with the dictionary.items() method.
"""


"""
#Okay the code below works. And it accurately makes complete full names.

employee_directory = {"Garcia": ["Bob", "Steven", "Mary"], "Parker": ["Peter", "Greg", "Sally"], "Rodriguez": ["Billy", "Melanie", "Zackariah"]}

#Okay before I start I need to find a way to cycle through the entire dictionary. 
#I'll need to cycle through each key,value pair. 
#I'll then need to cycle further through each 

full_name_list = []

for lastname, firstnames in employee_directory.items():
    for firstname in firstnames:
        full_name = firstname + " " + lastname
        full_name_list.append(full_name)

print(full_name_list)

"""

#Okay, let's create a function which ties all of this together.
def list_full_names(input_employee_dictionary):
    result_full_name_list = []
    for lastnames, firstnames in input_employee_dictionary.items():
        for firstname in firstnames:
            full_name = firstname + " " + lastnames
            result_full_name_list.append(full_name)

    return result_full_name_list 

employee_directory = {"Garcia": ["Bob", "Sally", "Miguel"], "Rodriguez": ["Mike", "Tally", "Taz"], "Smith": ["Billy", "Madision", "Sam"]}

print(list_full_names(employee_directory))




