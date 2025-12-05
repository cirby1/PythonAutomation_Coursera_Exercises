"""
#4. Fill in the blank to complete the even_numbers() function. This function should use a list comprehension to create a list of even integers using a conditional statement if statement with the modulo operator to test for numbers evenly divisible by 2. The function receives two variables and should return the list of even numbers that occur between the first and last variables exclusively (meaning don't modify the default behaviour of the range to exclude the "end" value in the range). For example, even_numbers(2, 7) should return [2, 4, 6]. 
"""

def even_numbers(first, last):
    return [num for num in range(first, last, 2)]



#print(even_numbers(4, 14))

print(even_numbers(0, 9))

print(even_numbers(2, 7))





