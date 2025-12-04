"""
2. Complete the for loop and string method needed in this function so that a function call like "alpha_length("This has 1 number in it.") will return the output "17". This function should:

1. Accept a string through the parameters of the function.
2. Iterate over characters in the string.
3. Determine If each character is a letter(counting only alphabetic characters, numbers, punctuation, and spaces should be ignored). 
4. Increment the counter.
5. Return the count of letters in the string. 
"""

def countTheLetters(input_string):
    letter_count = 0
    for individual_letter in range(0, len(input_string)):
        if input_string[individual_letter].isalpha():
            print(input_string[individual_letter])    
            print("This is considered a alphabetical character.")  
            letter_count += 1
            print("The letter count is:" + str(letter_count))
            print()
    return letter_count

print(countTheLetters("This has 1 number in it."))

"""
def alpha_length(string):
    character = ""
    count_alpha = 0
    # Complete the for loop sequence to iterate over "string".
    for individual_letter in range(0, len(string)): 
        # Complete the if-statement using a string method. 
        if string[individual_letter].isalpha():
            count_alpha += 1  
    return count_alpha
 
print(alpha_length("This has 1 number in it")) # Should print 17
print(alpha_length("Thisisallletters")) # Should print 16
print(alpha_length("This one has punctuation!")) # Should print 21




"""


