#Here we have to import regular expressions in order to use the package tools.
#import re

#print(re.search(r"[Pp]ython", "Python"))

#re.search is the action! It means to search for this regular expression inside of this string. 

# r " " means raw. So it will just be the raw string that is inserted in Python. 

# [Pp] means a range search for this. It's like a search filter.

#So basically it's searching for python or Python.

#In the string Python. 

#----------------------------------------------------------------------------------------------------

#Here again we have to import the regular expression package always. It's absolutely necessary.
#import re

#print(re.search(r"[a-z]way", "The end of the highway"))
#[a-z] means to search in this range of a through z.
#I guess it means any single letter from a to z. It's different from just using a "." which is just any character.
#So it means look for any word that has anyletter starting it and then "way" at the end of it.
#It does match "hway" for this.

#-----------------------------------------------------------------------------------------------------------------

#import re

#print(re.search(r"[a-z]way", "What a way to go"))

# r " " means raw string so it will just import the string raw as it is into Regular Expression.

#[a-z] means search for any character [a-z]. 

#So when it runs, "What a way to go", I don't think it will return any hits since there's a space before way. 

#------------------------------------------------------------------------------------------------------------------

#import re

#print(re.search("cloud[a-zA-Z0-9]", "cloudy"))

#Okay so it's the same pattern.
#Import re means to import regular expressions.
#re.search is the action, but we have to plug in the regular expression, and the string. 
#now "cloud" before the other stuff means just the text c l o u d. 
#After that we are looking for one character in any of these ranges. Either a through z, A through Z, or 0 through 9. 
#It actually matches.

#--------------------------------------------------------------------------------------------------------------------
#import re
#print(re.search("cloud[a-zA-Z0-9]", "cloud9"))

#Like before this is going to match the string cloud with any alpha character (upper or lower) or numbers 1 through 9. 
#It makes a match.

#import re

#print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))

#We first import regular expressions which is the package. To start. import re

#re.search is the action and we need to plug in the regular expression and the place where we want to search.

# r " " means Python ignore this and don't mess it up. Treat it as a raw string and then when we plug it in, Regular Expression will intepret it.

#[ ] means to filter and it's more like select a range inbetween these things.

#^ Means the front of the sentence. So search the first character at the front of the string?

#a-zA-Z mean any lowercase or uppercase letter.

#So this should technically get hit as "This" will match the capital T at the beginning.

#Okay so ^ has TWO DIFFERENT MEANINGS. Inside the brackets it means NOT. Outside it means look at the beginning of the line.

#So this means the first instance of anything that is not a letter. So it finds the first space character. 

#----------------------------------------------------------------------------------------------------------------------------

#print(re.search(r"cat|dog", "I like cats."))

#re.search is the action. Plug in the regular expression, and the thing you want to search.
#r " " is the raw string. It tells Python to ignore and not interpret this. So that the text isn't messed up being sent into re.
#cat|dog
#| means or I think, let me look online.
#Yes, I was right the | symbol means OR in regular expression.
#This is basically saying look for the words cat or dog in the sentence.

#-----------------------------------------------------------------------------------------------------------------------------

#This example is interesting. It ONLY matches the first instance of which it finds a hit. Which is dog.
#print(re.search(r"cat|dog", "I like both dogs and cats."))

#----------------------------------------------------------------------------------------------------------------------------

#print(re.findall(r"cat|dog", "I like both dogs and cats."))
#Okay so findall is really interesting. It just returns a list of all matches into a list. So in this case, dog and cat are put into a list. 


#-----------------------------------------------------------------------------------------------------------------------------

#Okay, I think I'm good now, lets go on to the next part...








