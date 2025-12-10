#You need to sort a list of strings based on their length. Which argument would you use?


strings = ["Abcdefghijkl", "123", "blahblah", "Bobby", "Aa", "xyz123xyz123"]


strings.sort(key=len)
print(strings)



#Okay, so I tried all of them and the one that worked out for me the best was: "key=len". 
