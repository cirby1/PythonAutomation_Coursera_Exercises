#Here is the reading exercises on splitting and replacing in regex. Here we gooooooohhhhhhhhhhhh!!!!!!!!!!!!!!!!!!

#We import re for all these examples, which imports the regular expressions packages for it's tools.
import re

#print(re.split(r"[.?!]", "One sentence. Another one? And the last one!"))

#re.split - What does that do? Okay, I think it breaks apart a string into pieces. What kind of pieces are dictated by what kind of regular expression you use and the program uses this as break points.

#r "" - like always this treats this string as raw for Python, so it doesn't interpret it, and then since we are inputting it into the regex, it will interpret it.

#[ ] - brackets mean a range filter. It will choose one thing in here and use it. It's almost like a buffet. 

#. means physical period. 

#? means physical question mark.

#! means physical exclamation point.

#Okay, when we run it. Something interesting really happens. It breaks apart the string by what was specified in our regex. Since we specified different punctuation symbols at the end of a sentence, that is where it is breaking. It then puts all these pieces into a list. 

#This could be really useful If I want to break apart a corpus of books by sentence. But I don't want the punctuation symbols at the end of the sentence.

#------------------------------------------------------------------------------------------------------------------------------------------------------------

#print(re.split(r"([.?!])", "One sentence. Another one? And the last one!"))

#Here the difference is that we are splitting based off of a group. It's grouping all the sentences based on punctuation marks first and then splitting them. And since the punctuation marks are grouped. It's saving them and then putting them into a list.

#------------------------------------------------------------------------------------------------------------------------------------------------------------

#print(re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for gonuts95@gmail.com"))

#Okay, now what does sub mean? It has to maybe mean substituted? I guess it will substitute the match for a string provided. Which is extremely, extremely handy. 

#[] is a buffet filter.
#\w is a word character.
#. is a physical period.
#% is a physical percentage sign.
#+ is a + eventhough I though it was supposed to be escaped?
#- is a minus sign.
#So overall it's gonna look for any of these characters and CHOOSE ONE to match. It's like a username finder for miscellanious cases. More than likely it will just find the \w character.
#Then there's a physical + on the outside meaning, one or more. So it will have to eat one or more of these symbols.

#@ is a physical @ symbol.

#[] now we have another brackets.
#\w word characters
#. physical period
#-

#Then after that the word REDACTED.

#So basically it looks for a word clump, another @ symbol, and then another word clump. And it picks up on the .com since it's looking for one or more of these symbols and picking up on periods too.

#=============================================================================================================================================================

print(re.sub("^([/w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace Ada"))

#re.sub - substitute a match in the string for another string that we choose.

#^ start of the string

#(capture group #1 

#[start of buffet filter

#\w is a word character

# .- are spaces, periods, and dashes.

#] end of buffet filter

#* zero or more matches

#)end of capture group 1

#So this first capture group is looking for word characters, spaces, periods or dashes. Names. At the beginning of the String. Any kind of name or funky name.

#, a physical comma

#Then we repeat again, a name or funky name until the end of the string.

#The next part though we are actually using the regex's capture groups to sub itself. Which is a neat trick. It just switches around the names and puts it as first name, lastname.





























