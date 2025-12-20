#Write a program that takes a log line. And extracts the Process ID number from it. Be sure to put this code into a function so that it's more efficient.
#The log is: "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade".
"""
import re

regex = r"\[(\d*)\]"

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"

match = re.search(regex, log)

print(match[1])

"""
import re
#Okay let's throw all of this into a function now. Haha!
str_text = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"

def extract_ProcessID(str_inputtext):
    regex = r"\[(\d*)\]"
    match = re.search(regex, str_inputtext)
    return match[1]

result = extract_ProcessID(str_text)
print(result)

#The only mistake I really made was using * instead of +. But both did the job.
