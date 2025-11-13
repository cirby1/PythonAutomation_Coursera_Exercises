#6 Fill in the blanks to complete the biography_list() function. This function reads in a list of tuples people, which contains the name, age, and profession of each person. Then, prints the sentence "___ is ___ years old and works as ___."

#For example, biography_list([("Ira", 30, "a Chef")]) and should print:

#Ira is 30 years old and works as a chef.

#Make sure there is a period at the end of each sentence. Otherwise, your response will be evaluated as incorrect.

#my_professionals_list = [("Bob", 30, "Chef"), ("Mike", 25, "Teacher"), ("Greg", 20, "Waiter"), ("Lance", 44, "Coach")]

#This should work then.
#for individual in my_professionals_list:
#    print(individual[0])


#for individual in my_professionals_list:
#    print("{} is {} years old and works as a {}.".format(individual[0], individual[1], individual[2]))

my_professionals_list = [("Bob", 30, "Chef"), ("Mike", 25, "Teacher"), ("Greg", 20, "Waiter"), ("Lance", 44, "Coach")]

#Okay all of the above works. Let's put it into a function.
def biography_list(input_tuple_list):
    for individual in input_tuple_list:
        print("{} is {} years old and works as {}.".format(individual[0], individual[1], individual[2]))
      
biography_list(my_professionals_list)


