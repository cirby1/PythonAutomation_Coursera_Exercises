#Okay here are my notes for the Review: Escaping Characters.

#import regular expressions
#import re

#print(re.search(r".com", "welcome"))
#Okay so "." means any character. And ".com" means any character plus "com". So I think it will get a hit because "lcome". 

#import re
#print(re.search("\.com", "welcome"))
#I feel like the \ means to escape the ".". So that means actually ".com" like at the end of a website. I don't think there will be any hits as "lcome" isn't the same as ".com". 
#So I ran it and yes there is no hits. 

#import re
#print(re.search(r"\.com", "mydomain.com"))
#Here we get a hit as expected since the escape ".com" matches the ".com" at the end of the website.

import re
#print(re.search(r"\w*", "This is a example"))
#Okay, I'm not really sure what's going on here... It's an escaped w and then there is * which means more or nothing. 

#So \w means word sequence. Any typical letter in a single word: A-Z (upper/lower), 0-9, or even _ underscore.
#So \d means any single digit.
#And \s mean whitespace. 
#So \w* together mean to grab the first word clump. 

print(re.search(r"\w*", "And_this_is_another"))

#So, w* will grab any word character until it reaches something which is not a word character like a space or a comma.
#So I'm forseeing that it will grab this entire sentence since there are no spaces and it has underscores which make it act like a username.



