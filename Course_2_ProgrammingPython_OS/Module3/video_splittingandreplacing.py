import re

print(re.split(r"the|a", "One sentence. Another one? And the last one!"))

#Okay, so this one is splitting by all occurences of lowercase a and lowercase the.

#There's a the in "Another" so it will split there.

#There's the word the after the word And.

#There's a lowercase a in the word last.

#One sentence. Ano r one? And l st one!

#So basically after taking out all those matches this is the results.
