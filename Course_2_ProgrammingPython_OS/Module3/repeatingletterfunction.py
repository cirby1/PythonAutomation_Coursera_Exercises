#The function checks if the text passed includes the letter 'a' (uppercase or lowercase) at least twice.


#Okay, the mistake I made is that I think I put A-Z instead of just Aa (Uppercase and lowercase).

import re

def repeating_letter_a(text):
    result = re.search(r"[Aa].*[Aa]", text)
    return result != None

#print(re.search(r"[Aa].*[Aa]", "bAnanA"))

#Okay we need to search for repeating letter a's. 
#We probably need to be greedy in our search?
#I'm thinking like a.*a?
#Let's try it and see what happens.
#Nope didn't quite completely work, it's not finding capitals. Maybe [A-Za-z].*[A-Za-z].

print(repeating_letter_a("banana")) #True

print(repeating_letter_a("pineapple")) #False

print(repeating_letter_a("Animal Kingdom")) #True

print(repeating_letter_a("A is for apple")) #True

#Okay, I think I got this right. Stepping through it helped me figure out what I was doing wrong. 



