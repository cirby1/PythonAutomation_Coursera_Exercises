import re
#Okay, so this is a log message and it's just a string. It's not very organized though. And kind of hard to read...
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"

#I guess this looks at the first position of where the error message starts. If the number has a pattern, then it will just be a couple of numbers.
index = log.index("[")

#Now this extracts the string based on the starting position that we got last time at "[" and then we are having to go up 6 places to strip away the error message number. It's just a little trick.
error_message = log[index+1:index+6]

print("Here's the first way to do it: ")
print(error_message)


regex = r"\[(\d+)\]"

#Okay, let's break down this regex expression.

#            r" "
#This means this is a raw string. Python ignore everything and just treat it like plain old text. Let me use my backslashes please and don't mess them up. 

#           \[
# Here we are actually escaping the character using regex and not python. Since [ and ] are so special in regex and are part of charactes sets. We are telling regex to look for the first instance of the character [ .

# [    ] are like a search filter
#Okay, just so we cover it. The [ and the ] mean in simple language: pick one from this list. Look at this spot and match exactly one character, as long as one of those things I put are inside of these brackets. 

# ( ) are like a storage bag.
#Take whatever you found in that spot and save it so that you can use it in your code later.

# d means a single digit.
#It means a single digit which could be 0, 1, 2, 3, 4, 5, 6, 7, 8, 9.

# + is like a greedy eater.
#It means to keep collecting the same of that thing and putting them into a chunk. And it will stop once it reaches something which is not that thing. In our case it will stop collecting once it reaches a character that is not a number. Which is what d+ or digit+ means.

# ^ has two separate functions. It usually means "look at the beginning" when it is outside of the brackets. Inside the brackets it means "NOT" so like [^a-z] means NOT a-z. 

#* means zero or more. It will accept a match or it will not accept a match.

#The + sign means a more stricter form of * it means one or more. Not one or more.

#The ? sign means optional so optionally look for the character preceding it. So p? means optional p.

#\w means any word sequence character and even underscores. It doesn't mean spaces or commas.
#\d means any single digit.
#\s means space.

# okay so a better way of looking at it is:     [       (    d+     )      ]
#or better yet:                                 [ get all the numbers here ]
#Or find as many digits in between the brackets. 
#And so this extracts that error message that we need between the brackets.

#Okay, the next step is the actual action step. 

#result = re.search(regex, log)
#print(result)
#result is just a variable that holds the answer and we are putting the answer into it with the = sign.

#re.search



