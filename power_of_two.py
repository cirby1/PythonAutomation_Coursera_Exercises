#This program checks if a number is a POWER of two. How does it do this? It will continue dividing by two until that number is one. The Program states that we need to avoid a ZeroDivisionError?

#Zero division error occurs when you try to divide a number by zero. You cannot divide anything by Zero. 

#Some conditions to check for:
#0/2 is False 
#1/2 should be True? I guess because 1 means that the original number is divisible by 2?

#So basically keep dividing until you don't see anything left over. 


print("Starting Program...")
print("")
number = 10

def is_power_of_two(number):
    print("inside the function")
    print("The number is: " + str(number))
    print("--------------------------------------")
    while number % 2 == 0 & number != 0:
        number = number / 2
        if number == 1:
            return True
    return False

    print("------------------------------------------")

print(is_power_of_two(9))


