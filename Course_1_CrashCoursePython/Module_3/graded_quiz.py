"""
#1 - Print the numbers 1 through 7.
number = 1 #Initialize the variable.
while number < 8: #Complete the while loop condition.
    print(number, end=" ")
    number += 1 #Increment the variable.
#It should print 1 2 3 4 5 6 7
"""

"""
#2 - The Loop should print every even number from 2 to 12. 
for number in range(1, 13):
    if number % 2 == 0:
        print(number)
"""

"""
#3 - Fill in the blanks to complete the function "digits(n)" to count how many digits the given number has. For example: 25 has 2 digits and 144 has 3 digits. Tip: you can count the digits by dividing it by 10 once per digit until there are not digits left. 

"""
"""
def digits(n):
    count = 0
    if n == 0:
        count += 1
    while n % 10 != 0: # Complete the while loop condition.
        #Complete the body of the while loop. This should include performing a calculation and incrementing a variable in the appropriate order. 
        if n % 10 == True:
            count += 1
            n = n / 10
        else:
            return count
    return count

#print(digits(25))
#print(digits(144))
#print(digits(1000))
#print(digits(0))
"""
"""
luckynumber = 25
CanItDivideBy10 = (luckynumber % 10 != 0)
print(CanItDivideBy10)
#We need to check checking until the number is depleted. 
#Cycle until the number is over.
    #Check can 10 go into it?
        #If so then keep tabs and subtract 10.
        #If not then we are done and it's just a single digit number. 
keepingcount = 0
while luckynumber > 0:
    if luckynumber < 0:
        break
    if (luckynumber / 10 != 0) & (luckynumber - 10 > 0):
        keepingcount += 1 #This means that the digit can be divided and so we keep count of the 1st digit.
        print(str(luckynumber) + " " +"The Lucky Number can be further divided by 10")
        luckynumber = luckynumber - 10
    else:
        keepingcount += 1
        print(str(luckynumber) + "" + "The Lucky Number is now a single digit.")
        break
print("Outside of the while loop.")

print("The count was " + str(keepingcount))
#3 - I added count+= 1 on lines line and n = int(n/10) on lines 10. 
#4 - I added the start and stop on lines 5 and 8. And I made sure to do +1 on the stop. 
"""

def counter(start, stop):
    if start > stop:
        return_string = "Counting down: "
        while start != stop or start == stop: #Complete the While Loop
            return_string = return_string + " " + str(start) #Add the numbers to the "return_string"
            if start > stop:
                return_string += ","
            start = start - 1#Increment the appropriate variable
    else:
        return_string = "Counting up: "
        while start != stop:#Complete the While Loop
            return_string = return_string + " " + str(start)#Add the numbers to the "Return String"
            if start < stop:
                return_string += ","
            start = start + 1#Increment the appropriate variable
    return return_string

#print(counter(1, 10)) #Should be "Counting up: 1,2,3,4,5,6,,7,8,9,10"
print(counter(2, 1)) #Should be "Counting up: 1,2,3,4,5,6,,7,8,9,10"
#print(counter(5, 5)) #Should be "Counting up: 1,2,3,4,5,6,,7,8,9,10"
















