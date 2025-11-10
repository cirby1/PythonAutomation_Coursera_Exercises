"""
#1 - Recursion is used for calling a function inside the same function.
#2 - Which of these activities are good use cases for recursive programs: I chose A, D.
#3 - Recursive Programs

#This program should return whether the number is a power of a given base.
# inputs are (8 is the number, and 2 is the base?) Also, (64 is the number and 4 is the base).
# 8 / 2 = 4.....    4 / 2 == 2 .....  2 / 2 == 1...
#64 / 4 is 16... 16 / 4 is 4....  4 /4 = 1
#Once the division reaches 1, that means it's power. 


#70 is the number and 10 is the base.
#70 / 10 = 7... 7 / 10 == 3/10 so no. 70 isn't a power of base 10. Base 10 is 10, 100, 1000, 10,000 etc...
inputnumber = 0
inputbase = 0

def powerof(inputnumber, inputbase):
    comparison = inputnumber / inputbase
    if comparison  == 1:
        #If they divide into 1, then that means we are done and it is a power. For example 4/4 equals 1. 
        return True
    if inputnumber > inputbase:
        inputnumber = inputnumber / inputbase
        return powerof(comparison, inputbase)
    if comparison < 1:
        return False

print(powerof(8, 2))
print(powerof(64, 4))
print(powerof(70, 10))

#Recursion is a process where a function calls itself one or  more times with modified values to acoomplish a task. This technique can be particularly effective when solving complex probles that can be broken down into smaller, simpler problems of the same type. In the provided code, the count_users function uses recursion to count the number of users that belong to a group within a company's system, it does this by iterating through each member of a group, and if a member is in another group, it recursively calls count_users to count the users within that subgroup. However, there is a bug in the code! Can you spot the problem and fix it?

def count_users(group):
    count = 0
    for member in get_members(group): #Iterate through each member of a group.
        count += 1
        if is_group(member): #If member is in another group.
            count+= count_users(member) #Recursively calls count_users to count the users with that subgroup.
    return count

print(count_users("sales"))

#The probelm is that you are counting each member even if it's a group. The code should be if they're in a group, then keep digging. Otherwise, count that person as member. 

"""
#In the while loops, you were aksed to write a function to calculate the sum of all positive numbers between 1 and n. Rewrite the function using recursion instead of a while loop. Remember that when n is less than 1, the function should return 0 as the answer.

def sum_positive_numbers(n):
    sum = 0
    if n < 1:
        return 0
    for i in range(1, n+1):
        sum = sum + i
    return sum

print(sum_positive_numbers(3))
print(sum_positive_numbers(5))




