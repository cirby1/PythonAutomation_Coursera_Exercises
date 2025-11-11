#Fill in the blanks to complete the "even_numbers" function. This function should return a space-separated string of all positive numbers, excluding 0, up to and including the "maximum" variable that's passed into the function. Complete the for loop so that a function call like "even_numbers(6)" will return the numbers "2 4 6".
def even_numbers(maximum):

    return_string = "" #Initializes variable as a string


    #Complete the for loop with a range that includes all even numbers up to and including the "maximum" value, excluding 0. 
    for i in range(1, maximum+1):
        if i % 2 == 0: #Check if it's an even number
        #Complete the body of the loop by appending the even number followed by a space to the "return_string" variable.
            return_string = return_string + str(i) + " "


    #This .strip command will remove the final " " space at the end of the "return_string".
    return return_string.strip()

print(even_numbers(6))

#This solution works so I'm pasting it in and seeing how it goes!!!
