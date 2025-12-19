#Here we always import the regular expressions module
#import re

#result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
#Okay since there's a ^ at the beginning and a $ at the end. The capture or match will run from the beginning of the string to the end.
#() means a storage container or group. 
#\w means alpha characters or word characters.
#* means get as many as possible until you cannot.
#, the comma is as is. So it's a physical comma.
#And then afterwards it repeats the same group from before.
#So basically it's two word groups separated by a comma.

#This just prints the resulting match.
#print(result.group())
#print(result.groups())

#Okay so after researching it, the .group() and .groups() commands are linked to the parentheses groups in the regex! With .group() too you can put a number starting at 0 and it will return the group at that location. If nothing is provided it will just default to showing everything. .groups show everything by default as a tuple list. .group shows everything as a long string.

#Okay, so as I expected. Indexing the regular expression matching function returns strings. If 0 is supplied it returns .group() or the whole thing. Then after that you can put 1, 2, 3 etc. This will allow you to see different groups of strings in order. It will show the first string inside the first set of ().     
#print(result[0])
#print(result[1])
#print(result[2])

#This, I don't know what this is. They are just printing the 2nd string in the tuple of results. Which is Ada and then the output of results. Oh wait nevermind, I forgot the index on the second result variable. It's supposed to output the full name. 
#print("{} {}".format(result[2], result[1]))
