#Okay so here we are going to iterate through all the books. And I'm gonna change all the lines to Upper case.

#Remember, you can use the with open command and then for loop through each line.  

with open("allbooks.txt") as allpbbooks:
    for line in allpbbooks:
        print(line.upper())

#Okay, let me run it and see if it outputs as upper. This will be handy for cleaning the text up as I can revese it and make it all lower if needed. 

#Yup! It did it! And it did it quickly.
