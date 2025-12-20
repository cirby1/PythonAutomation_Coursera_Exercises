import re
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])

#import re = import the regular expression module for the package tools.
#log = Just the text string of the log error that we need to search through.
#regex variable to store the raw string regular expression.
#\[ means a physical brackets.
#() means a group.
#\d means a digit character so basically a number.
# + means one or more repeat match.
#\] another physical other side of a bracket.
#Basically it's looking for a number inbetween two brackets. And since the number inside is group, you can use the re search group function to output just the number in parentheses since it's in a group.




