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

def count_departments(dict_employee_departments):
    #The input is a dictionary which has data about employees.
    #The output is a dictionary that has a department and it's count. 
    department_counter = {}

    for individual_employee in dict_employee_departments:
        department = individual_employee["department"]
        if department in department_counter:
            department_counter[department] += 1 
        else:
            department_counter[department] = 0  
            department_counter[department] += 1
    return department_counter


#Okay the two lines below are needed to run. First you need to run the first function to get the employee worker list. And then you plug that into the next function which is above which is count departments. It all checks out and works.
employee_departments = create_work_dictionary("/home/calvinirby01/PythonAutomationExercises/Course_2_ProgrammingPython_OS/Module2/Qwiklabs_RetroBusinessDepartments/retrorickdepartments.csv")
department_counter = count_departments(employee_departments)


def make_Report(str_department_counter):
    #The input is the department list of counts from before.
    #The output is a report file that is made into a text file.
    print("The output for the report is: \n")
    for individual_department, number in department_counter.items():
        print(individual_department + " " + str(number))

    with open("RetroRicksReport.txt", "w") as file:
        for individual_department, number in department_counter.items():
            file.write(individual_department + " " + str(number) + "\n\n")
    print()
    print("Your data was saved into the external file successfully.")


make_Report(department_counter)











