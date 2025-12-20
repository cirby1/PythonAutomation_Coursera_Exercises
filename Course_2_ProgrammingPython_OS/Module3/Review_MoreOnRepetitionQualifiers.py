#Import regular expressions as a module always so we can use the package regular expressions tools. 
#import re
#print(re.search(r"[a-zA-Z]{5}", "a ghost"))
#r "" - means raw string
#[] - filter and select one
#a-zA-Z - any letter upper or lower
#{5} - means times 5.
#So overall it's going to scan and find at least a 5 letter chunk word.

#Import regular expressions as a module so we can use the re tools.
#import re
#print(re.search(r"[a-zA-Z]{5}", "a scary ghost appeared"))
#r " " - raw string. 
#[a-zA-Z] - this meeans any letter upper or lower.
#{5} - means times 5
#I believe this will just capture the first instance of the match. So yes, in this case it's 'scary'. 

#Import the re package which is regular expression package so that I can use the tools.
#import re
#print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared"))
#re.findall -  I think lists all the matches. Yes, I ran it and it does. It lists as many matches as possible.
#[a-zA-Z] - means any alphabetical character either uppercase and/or lowercase. 
#{5} - This means find five occurences of the previous thing.
#So overall it's looking for a five letter word occurences. And outputting them all.
#print(re.search(r"[A-Za-z]{4}\s[A-Za-z]{4}\s[a-z]\s[a-z]{4},", "Once upon a time,"))

#import re
#print(re.findall(r"\b[a-zA-Z]{5}\b", "A scary ghost appeared"))
#\b means word boundary, so it means one the left or right side of a word.
#[a-zA-Z] any characters a through z either capitalized or lowercase.
#{5} means to repeat 5 times.
#\b other side of word boundary.
#So overall it's ignoring matches within words and focusing on one complete word that is five characters long. 

#Import regext to start using.
#import re   
#Print all the resulting matches.
#print(re.findall(r"\w{5,10}", "I really like strawberries"))
#Regular expression and find all the matches and return them all.
#\w is a word characte
#{5,10} means find 5 to 10 characters.

#import re
#print(re.findall(r"\w{5,}", "I really like strawberries"))
#\w means word characters.
#{5,} means 5 or more?

import re
print(re.search(r"s\w{,20}", "I really like strawberries"))
#s I think means physical s.
#\w means word character.
#{,20} means from 1 to 20?







