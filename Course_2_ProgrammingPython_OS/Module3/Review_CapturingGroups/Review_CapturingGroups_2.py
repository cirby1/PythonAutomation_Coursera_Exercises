#Here we always import the regular expression module so that we can start using the regular expression package tools.
import re

#Here we define a function name. It's called rearrange name, and I guess it just mixes up a name for us.
def rearrange_name(name):
    result = re.search(r"^(\w*), (\w*)$", name)
    #r " " means raw
    #^means start of string match
    #$means end of string match
    #The match has to go from start of the string to the end.
    #() means group
    #\w means word character
    #* means greedy clump
    #So it's a group of word characters
    # a physical comma
    #And another group of word characters

    #If the result is non matching it will just return the name back to us.
    if result is None:
        return name
    #If it is matching then, It will take the second string in the tuple and then the first string in the tuple and switch them around.
    return "{} {}".format(result[2], result[1])
print(rearrange_name("Lovelace, Ada"))


