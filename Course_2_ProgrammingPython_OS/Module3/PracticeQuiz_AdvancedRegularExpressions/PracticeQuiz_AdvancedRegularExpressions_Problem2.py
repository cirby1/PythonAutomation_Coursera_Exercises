#2 - The multi_vowel_words() function returns all words with 3 or more consecutive vowels (a, e, i, o, u). Fill in the regular expression to do that. 
import re

def multi_vowels(text):
    pattern = r"\b\w*[aeiou]{3}\w*\b"
    result = re.findall(pattern, text)
    return result




print(multi_vowels("Life is beautiful"))
# ["beautiful']

print(multi_vowels("Obviously, the queen is courageous and gracious."))
#['obviously', 'queen', 'courageous', 'gracious']

print(multi_vowels("The rambunctious children had to sit quietly and await their delicious meal."))

print(multi_vowels("The order of a data queue is First In First Out (FIFO)"))

print(multi_vowels("Hello world!"))





