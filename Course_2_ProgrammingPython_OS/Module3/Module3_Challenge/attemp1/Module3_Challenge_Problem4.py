#4 - You are exploring the punctuation at the end of the sentence and want to split sentences so that each word is separate and any punctuation is included in the word next to it. Complete the parse_sentence() function to accomplish this task.

import re

def parse_sentence(sentence):
    pattern = r"\s" #enter the regex pattern here.
    result = re.split(pattern, sentence) 
    print(result)
    return result

print(parse_sentence("Hello! How are you doing?"))

#I thin I was overthinking this one. Each word has to SEPARATE and can include the punctuation that is has.
