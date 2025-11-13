#3 Create a function that turns text into pig latin. Pig Latin is a simple text transformation that modifies each word by 1. Moving the first chracter to the end of each word; 2. Then appending the letters "ay" to the end of each word. For example, "python" ends up as "ythonpay". Make sure that there is no trailing whitespace at the end of the return output.

def turn_text_into_piglatin(inserted_text):
    #Okay, here's my code, I cleaned it up a bit from the below code...
    removed_letter = inserted_text[0]
    new_inserted_word = inserted_text[1:]
    second_step_word = new_inserted_word + removed_letter
    endresult = second_step_word + "ay"
    return endresult

"""
#No I need to cycle through each word and apply the pig latin to the words.
mysent = "Today is a great day."
print(mysent)
newsent = mysent.strip()
print(newsent)
"""
"""
#The problem that I was doing was that I was using the strip() function and not split()!!! Wrong one!!!
mysent = "programming in python is fun"
splitup_sentence = mysent.split()
print(splitup_sentence)
for individual_word in splitup_sentence:
    print(individual_word)
"""
"""
mynewsentence = []
for individual_word in splitup_sentence:
    piglatinword = turn_text_into_piglatin(individual_word)
    mynewsentence.append(piglatinword)
print(mynewsentence)

mycleansentence = ""
for individualword in mynewsentence:
    mycleansentence = mycleansentence + " " + individualword 
print(mycleansentence)
"""

def turn_sent_into_piglatin(inserted_sentence):
    result_list = []
    result_sentence = ""
    split_sentence = inserted_sentence.split() 
    for individual_word in split_sentence:
        result_list.append(individual_word)
    for individual_word in result_list:
        piglatinword = turn_text_into_piglatin(individual_word)
        result_sentence = result_sentence + " " + piglatinword
    return result_sentence

print(turn_sent_into_piglatin("hello how are you"))
print(turn_sent_into_piglatin("programming in python is fun"))

"""
mytext = "python"
print(mytext)
print(mytext[0])
first_letter = mytext[0]
my_removed_firstletter_word = mytext[1:]
print(my_removed_firstletter_word)

second_step_attachedletterend = my_removed_firstletter_word + first_letter
print(second_step_attachedletterend)
added_ay_ending = second_step_attachedletterend + "ay"
print(added_ay_ending)
added_ay_ending = added_ay_ending.strip()
print(added_ay_ending)
"""





