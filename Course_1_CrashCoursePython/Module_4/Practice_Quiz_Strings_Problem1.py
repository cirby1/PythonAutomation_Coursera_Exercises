#1. Fill in the blanks to complete the is_palindrome function. This function checks if a given string is a palindrome. A palindrom is a string that contains the same letters in the same order, whether the word is read from left to right or right to left. Examples of palindromes are words like kayak and radar, and phrases like "Never Odd or Even". The function should ignore blank spaces and capitalization when checking if the given string is a palindrome. Complete this function to return True if the passed string is a palindrome, False if not. 

def is_palindrome(input_string):
    #Two Variables are initialized as string date types using empty quotes: "reverse_string" to hold the "input_string" in revese order and "new_string" to hold the "input_string" minus the spaces between words, if any are found. 
    new_string = ""
    reverse_string = ""

    #Complete the for loop to iterate through each letter of the "input_string".
    for single_character in input_string: #Okay, I got the for loop to loop through every character in the string too.

        # The if-statement checks if the "letter" is not a space.
        if single_character != " ":
            
            #If True, add the "letter" to the end of "new_string" and to the front of "reverse_string" If False (if a space is detected), no action is needed. Exit the if-block.
            new_string = new_string + single_character
            reverse_string = single_character + reverse_string
        new_string = new_string.lower()
        reverse_string = reverse_string.lower()
        #print(new_string)
        #print(reverse_string)
        #print()
    #Complete the if-statement to compare the "new_string" to the "reverse_string". Remember that Python is case-sensitive when creating the string comaprison codde.
    #print(new_string)
    #print(reverse_string)
    if new_string == reverse_string:

            # If True, the "input_string" contains a palindrome.
            return True

    #Otherwise, return False.
    return False

print(is_palindrome("Never Odd or Even")) #Should be True.
print(is_palindrome("abc")) #Should be False.
print(is_palindrome("kayak"))

#Okay, I was able to do it by lowering all the case of all the words for comparision. I think it wasn't working because it was comparing Upper case to Lower case letters.








