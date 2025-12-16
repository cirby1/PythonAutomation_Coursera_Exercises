#Okay, now we are in the writing part. So far I learned how to read() a file, close() a file, readlines() from a file, sort() a file and these all did different things. Read() will read the file all at once. Close() will close the file and get it out of memory. The "with open("filename") as newfilename: " command opens and reads the file, and then once it exits the with structure it closes it. I can cycle through each line with a "for line in filename" command. 

#So all of these read a file. Now If I need to write to a file. Say, take one text from one and then put it into another text, then this is very, very useful.  

#I'm guess we use the with command, yet we have to specify that we want to write with the "w" operator. 
with open("mynewwritefile.txt", "w") as writtenfile:
    writtenfile.write("Hi, I think is a new book that I'm writing. Haha!")

#Okay, so I used cat it output the file's contents and the changes I made there worked. 

#There's several modes for the open function. 

#R Mode is the reading mode which is the default mode. 

#W Mode is write mode. 

#X Mode is for exclusive creation. Failing if the file exists.

#A is an appending mode and appending to the end of the line.

#+ Mode is both for reading and writing. 

#Okay encoding. I remember that when I was reading all the books in FreeBSD, the encoding was a different encoding. And the different encodings affect the different type of experience I will have working with the file. I believe utf-8 is the standard default encoding for text files. 

#Here's an example:
myfile = open("workingwritingfile.txt", "w", encoding="utf-8")


#So the biggest take away is that you will use the open() function to read/write files. The two arguments that are needed for the open function are the filename, the mode, and the encoding. The encoding is usually "t" by default which is utf-8 which is the standard. Remember you can also add a filepath instead of the just the filename. 

































