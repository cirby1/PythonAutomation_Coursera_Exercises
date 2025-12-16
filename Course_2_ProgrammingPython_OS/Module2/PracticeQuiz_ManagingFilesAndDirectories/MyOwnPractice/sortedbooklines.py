#Okay, next we are going to use the sorted method to sort through files.

#What's the first thing we have to do. Well we have to use the with open line as line. 


#Okay, here we are going to use the readlines command. The readlines command is interesting because it returns each line into a list. 

with open("allbooks.txt") as allfivebooks:
    booklines = allfivebooks.readlines()
    booklines.sort()
    print(booklines)

#Okay this returns a huge amount of text. And it puts all the lines into a list and then the .sort command sorts them in alpha order so that it's in alphabetical order.
