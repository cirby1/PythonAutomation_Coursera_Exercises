#Some stuff goes here.
"""
for n in range(19):
    if n % 2 == 0:
        print(n)

for x in range(1, 10):
    print(x**3)


for n in range(0, 100, 7):
    if n % 7 == 0:
        print(n)

input = "Four score and seven years ago"
for c in input:
    if c.lower() in ['a', 'e', 'i', 'o', 'u']:
        print(c)
#Messed up on 3,4, and 6.
#1 - C - while loops iterate while the condition is true; for loops iterate through a sequence of elements. 
#2 - B - for n in  range(6, 18+1, 3):
             #print(n*2)
#3 - Missing some.
#4 - Missing some code. 

#4 code
for x in range(1,10,1):
    if x % 3 == 0:
        print(x)
#5 code
for n in range(0, 100, 7):
    if n % 7 == 0:
        print(n)

input = "Four score and seven years ago"

#6
for c in input:
    if c.lower = ['a', 'e', 'i', 'o', 'u']:
        print(c)

print([c for c in input if c.lower() in ['a', 'e', 'i', 'o', 'u']])

A & B work, not c.. I don't think D works either...

#This one doesn't work because it's cycling through the numbers of the range of the message. Not the letters.
for c in range(len(input)):
    if c in ['a', 'e', 'i', 'o', 'u']:
        print(c)

#7 Which of these statements is true about slicing strings:
    C - starting index is negative, Python counts backwards from end of string.


for n in range(19):
    if n % 2 == 0:
        print(n)
#3 This one for also works...
for n in range(10):
    print(n+n)
"""
