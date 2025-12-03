#Use a list comprehension [] as a shortut for creating a new list from a range.
#Include a calculation with a for loop in a range with 2 parameters (lower,upper+1).

mylist = ["Alpha", "Boy", "Clark", "Dividends", "Evergreen"]

start = 10
end = 20

mynewlist = [number for number in range(start, end)]
print(mynewlist)

#Okay, I think this definitely worked. 
#And of course you can make a function and just have it plug in the starting number and where you want it to end.
