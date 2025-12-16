#!/usr/bin/env python3
import csv

def create_work_dictionary(str_filepath):
    #The input is a string which is a filepath to a csv file of employee data.
    #The output is a dictionary which is the employee records.
    with open(str_filepath) as rickdepartments:
        department_dictionary = csv.DictReader(rickdepartments)
        worker_list = []
        for row in department_dictionary:
            worker_list.append(dict(row))
        return worker_list

#Run the function create_work_dictionary below by uncommenting. It seems to work. And make sure you have the complete absolute path to a csv file of employee data. Our csv file was simple that just had fullname, username, and department.
#print(create_work_dictionary("/home/calvinirby01/PythonAutomationExercises/Course_2_ProgrammingPython_OS/Module2/Qwiklabs_RetroBusinessDepartments/retrorickdepartments.csv"))



"""

    print() 
    print()
#Okay, now we need to process the data or count who's in what I guess. Well I know I'm counting by department right?  

#Let me think, how can we cycle through a list... I guess with another for loop.
department_counter = {}

for individual_employee in worker_list:
    print(individual_employee)
    #Maybe this will print the entire row?
    department = individual_employee["department"]
    if department in department_counter:
        print("Adding a increment to the department: " + str(individual_employee["department"]) + "\n")
        department_counter[department] += 1 
    else:
        print("Made the department " + str(department))
        department_counter[department] = 0  
        print("Adding the increment to the department: " + str(department) + "\n")
        department_counter[department] += 1

print(department_counter)
print()
print("OKAY, THE FINAL REPORT IS BELOW. YIPPPPEEEEEE\n")

#Okay good! Now let's cycle through each element in the dictionary and print out the departments and numbers
for individual_department, number in department_counter.items():
    print(individual_department + " " + str(number))

#Okay now that I'm able to print out the results. Let's write it out to an external file.
with open("RetroRicksReport.txt", "w") as file:
    for individual_department, number in department_counter.items():
        file.write(individual_department + " " + str(number) + "\n")


#And that's really it. I think I'm getting the hang of it. Let's seal the deal and put all of my work inside of functions now.
#I'll need to make another file to do this and clean it up.




"""
