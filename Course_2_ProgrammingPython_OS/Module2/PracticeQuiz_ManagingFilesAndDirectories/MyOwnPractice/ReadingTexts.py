#Okay, here I'm gonna practice reading texts. I think I just need a little bit more familiarity with these topics. And the only way is to do it in my own special way!

fivebooks = open("allbooks.txt")

#Okay so this readline command takes bits and pieces and reads the lines one by one. 
#Here I see the title for the author's book.
print(fivebooks.readline())

#This is actually printing a blank line. It kind of threw me off. 
print(fivebooks.readline())

print(fivebooks.readline())

#This mega command reads the entire file and returns it as a string.
entirefivebooks = fivebooks.read()

print(entirefivebooks)

#Okay, so supposedly, If we are dealving into secret texts and books and stuff, you don't want your system memory to have that still lurking around. So you can use the fivebooks.close() command to close the file. 

entirefivebooks.close()
















