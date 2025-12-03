#use the len function to measure a string.

mystring = "Hello there is a new sale at Costco!"
print(mystring)

my_split_string = mystring.split()
print(my_split_string)

length_of_string = len(my_split_string) 
print(length_of_string)

#Okay, so now I know that it works. Let's put it into a function!!!
print("Start Program Here...")
def split_er_up(input_string):
    splitted = input_string.split()
    sizestring = len(splitted)
    return sizestring

print(split_er_up(mystring))

#Okay it works. Onto the next Coding Skill...
