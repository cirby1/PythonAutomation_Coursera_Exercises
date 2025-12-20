#Import regular expressions package to start using the package system tools.
import re

#Log message string to look through and find a process id to match.
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"

#The meat and potatoes of the whole program which is the regular expression that will search for a process id number.
regex = r"\[(\d+)\]"

#The action in which you use a regular expression on a log message.
result = re.search(regex, log)

#Another search in which they are looking for more process ids. I'm not sure If the previous results will actually save...
#Okay so results IS being overwritten. HOWEVER, the reason why we are printing the capture group at position 1 is so that we can get the numbers within the parenthesis. If it was result[0] it is the process id with the brackets. If it is instead result[1] then it is the number that is inside of it.
result = re.search(regex, "A completely different string that also has numbers [345678]")
print(result[1])


