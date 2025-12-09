"""
Complete the function so that input like "This is a sentence." will return a dictionary that holds the count of each letter that occurs in the string.

1. Accept a string "text" variable through the function's parameters.

2. Iterate over each character the input string to count the frequency of each letter found, do not count spaces, numbers or punctuation. 

3. Populate the new dictionary with the letters as keys, ensuring each key is unique, and assign the value for each key with the count of that letter. 

4. Return the dictionary.
"""

#def letterCounter(input_sentence):
letterCountDictionary = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I":  0, "J": 0, "K": 0, "L": 0, "M": 0, "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0, "U": 0, "V": 0, "W": 0, "X": 0, "Y": 0, "Z": 0, "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h" : 0, "i" : 0, "j" : 0, "k" : 0, "l" : 0, "m" : 0, "n" : 0, "o" : 0, "p" : 0, "q" : 0, "r" : 0, "s" : 0, "t" : 0, "u" : 0, "v" : 0, "w" : 0, "x" : 0, "y" : 0, "z" : 0}
#if "A" in letterCountDictionary:
#    print("True")

mystring = "Hello"
mystring.lower()
mystring.split()

for i in range(0, len(mystring)-1):
    print(mystring[i])
    if mystring[i].isalpha:
        letterCountDictionary[mystring[i]] += 1

print(letterCountDictionary)

"""
    for individual_character in range(0, len(input_sentence)):
        print(input_sentence[individual_character])
        if input_sentence[individual_character].isalpha():
            letterCountDictionary.update 

    print(input_sentence.split()) 

letterCounter("This is a sentence.")
"""

"""
#Well somehow I made the program work. Let me paste the one from the official problem below: 
def count_letters(text):
  # Initialize a new dictionary.
  dictionary = {}
  # Complete the for loop to iterate through each "text" character and
  # use a string method to ensure all letters are lowercase.
  text.split()
  text = text.lower()
  for i in range(0, len(text)):
    # Complete the if-statement using a string method to check if the
    # character is a letter.
    if text[i].isalpha():
      # Complete the if-statement using a logical operator to check if
      # the letter is not already in the dictionary.
      if text[i] not in dictionary:
           # Use a dictionary operation to add the letter as a key
           # and set the initial count value to zero.
          dictionary[text[i]] = 0
      # Use a dictionary operation to increment the letter count value
      # for the existing key.
      dictionary[text[i]] += 1
  return dictionary

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}
"""
