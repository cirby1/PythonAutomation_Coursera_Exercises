#Here I just import the os module which is a trick way of using unix commands inside of python. That's all. I just did it out of habit.
import os

#with open("allbooks.txt") as allmybooks:
#    print(allmybooks.readline())

#Now the above is kinda like what we did before, with readline, but it opens and closes a file for me. So it would be more efficient. In the future you just want to use this. Let me practice again beloww....


with open("allbooks.txt") as allmybooks:
    print(allmybooks.readline())


#So now I think I understand. Instead of having to open. Read the lines and then close. I can just use this with open() as name: line and do the same thing. Better yet, it closes it for me once it exits, so I don't have to remember to do it. 


















