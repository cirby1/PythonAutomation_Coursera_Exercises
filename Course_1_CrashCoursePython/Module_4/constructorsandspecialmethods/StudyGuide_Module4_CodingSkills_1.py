"""
Skill 1: Using String methods.
-#1. Separate numerical values from text values in a string using .split().
-#2. Iterate over the elements in a string. 
-#3. Test if the element contains letters with .isalpha().
-#4. Assign the elements of the split string to new variables. 
-#5. Trim any extra white space using .strip(). 
-#6. Format a string using .format() and {} variable placeholders. 
"""


"""
#1 - Separate numerical values from text values using .split().************************
#Okay, let's go through and practice doing each of these things...
mystring = "abc123"
newstring = mystring.split()
print(mystring)
#The data that is being input is a sentence, such as "Winter fleece jackets 49.99". 
#Strings really don't like mixed letters and numbers, because otherwise you would have to use regex to separate them. 
adsentence = "Wonderful Fleece Coats for 99.99"
mysplitsentence = adsentence.split()
print(mysplitsentence)
#The output would be: ['Wonderful', 'Fleece', 'Coats', 'for', '99.99']
"""

"""
#2 - Iterate over the elements of a string. 
mystring = "abcdefghi"
for individual_letter in mystring:
    print(individual_letter)
#Okay, I think I did this here. 
"""

"""
#3. Test if the element contains letters with .isalpha().
myletters = "abc"
mynumbers = "123"
print(myletters.isalpha())
print(mynumbers.isalpha())
#The following prints True for the first statement and then false for the second. 
"""

"""
#4. Assign the elements of the split string to new variables. 

mystring = "New Winter Coat 999"
mysplitstring = mystring.split()
print(mysplitstring)

mytext = ""
mynumbers = ""

for individual in mysplitstring:
    if individual.isalpha():
        mytext = individual
        print(mytext)
    else:
        mynumbers = individual
        print(mynumbers)

print()

print(mytext)
print(mynumbers)


#Okay, I think this kind of does this. It goes through and sees if the element is a letter or number and stores it appropriately. 
"""

"""
-#5. Trim any extra white space using .strip(). 
mystring = "haha "
print(len(mystring))
print(mystring)
mystripedstring = mystring.strip()
print(len(mystripedstring))
print(mystripedstring)
Okay, I made it work by using the length command function since White space is a character and it counts to the length of a string. 
"""

"""
-#6. Format a string using .format() and {} variable placeholders. 

#Okay for this one I will need to be able to make a sentence that says the name of the thing is this and it cost this.


thename = "Sweater"
thecost = "98"

mynewstring = "The cost of the {} is {} dollars.".format(thename, thecost)
print(mynewstring)

Okay, I think this worked fine. I just need to remember to initialize the string like I usually do and just stick the format function at the end with the plugs of the variables. 

"""
