import re


#The .* here means whatever in between. So it is a hit with the full word.
#print(re.search(r"Py.*n", "Pygmalion"))

#This one is really interesting. It doesn't stop at the 'n' in Python. It keeps going swallowing up more text and it stops only until it finds the "last" n in the sequence. It will go all the way to "The End" of a book for example, since it's so greedy.  
#print(re.search(r"Py.*n", "Python Programming"))

#print(re.search(r"Py[a-z]*n", "Python Programming"))
#Okay this one lookds for a string that starts with Py.
#Then it looks for one alphabetical lowercase character.
#Then we have the *here and I think it means "zero or more". So either it's a match or not a match. And it moves on. 
#print(re.search(r"Py[a-z]*n", "Pyn"))

#----------------------------------------------------------------------------------------------------------------------------

#import re
#print(re.search(r"o+l+", "goldfish"))
#So I'm guess o plus zero or more characters plus l plus zero or more characters.
#This would get a hit because there's nothing between o and l. And there also is nothing after l as well.

#print(re.search(r"o+l+", "woolly"))
#This one should return a hit. Since ooly matches the criteria which is o plus one or more plus l plus one or more.
#It looks for a cluster of o's and a cluster of l's. 

#print(re.search(r"o+l+", "boil"))
#This returns none. Since there is no repeating o's after the first o found. and there's no repeating l's after the first l found. 

#import re
#print(re.search(r"p?each", "To each their own"))
#Here we find that it searches for p? as a optional character, If it doesn't find it, it still looks for each. Which is in fact in the string. So it just returns a match for each.

#print(re.search(r"p?each", "I like peaches!"))












