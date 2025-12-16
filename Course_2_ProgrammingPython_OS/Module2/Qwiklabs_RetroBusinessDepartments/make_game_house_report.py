#Here I will make my program which will take Retro Rick's staff and turn it into a nice report.  

#Since this is an automation course I will need to put a shebang line. This is good because it will make my program an executable and the os will know what programming interpreter to use: bash, c, python. Etc.. etc...

#!/usr/bin/env python3

#Need to import csv as this is the tool that will help us the most.
import csv

print("Start of Program...\n")
print("Hello! We are gonna take Retro Rick's Department Data and turn it into a list just showing how many people are in each department, let's go!\n")

#Okay, this really isn't too bad and just the same thing we've been doing it. 
#I use the with open csv file and give the csv file a nickname: My nickname is ricksdepartments.
with open("/home/calvinirby01/PythonAutomationExercises/Course_2_ProgrammingPython_OS/Module2/Qwiklabs_RetroBusinessDepartments/retrorickdepartments.csv") as rickdepartments:
    #Then I have to use the csv DictReader function. And I read in the rickdepartments. Now it's memory. After that we just always use a for loop whether it's cycling through a text file or through a dictionary. 
    department_dictionary = csv.DictReader(rickdepartments)
    #Let's make a storage list for our data that we are going to cycle through and take.
    worker_list = []
    #We are going to take each row in the dictionary, and put it into the list. 
    for row in department_dictionary:
        worker_list.append(dict(row))
    print("WORKER LIST BELOW:****************")
    print(worker_list)
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
