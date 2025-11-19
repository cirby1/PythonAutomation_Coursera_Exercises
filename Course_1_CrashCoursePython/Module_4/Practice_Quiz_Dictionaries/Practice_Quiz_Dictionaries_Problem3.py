#3 The dict.update method updates one dictionary with the items coming from the other dictionary, so that existing entries arereplaced and new entries added. What is the content of the dictionary "wardrobe" at the end of the following code?

wardrobe = {"shirt": ["red", "blue", "white"], "jeans": ["blue", "black"]}
print(wardrobe)

new_items = {"jeans": ["white"], "scarf": ["yellow"], "socks": ["black", "brown"]}
print(new_items)

wardrobe.update(new_items)
print(wardrobe)

#Jeans will get white, blue, and black.
#New key scarf with values
#New key socks with values?

#shirt, jeans, scarf, socks
#shirt[red, blue, white], jeans[white,blue,black], scarf[yellow], socks[black,brown]
#No I was wrong it completely replaced the key with all the values of the next dictionary. They all got wiped and replaced with just "white" for jeans. 


#The answer I am putting is B. Which matches when I run the code. 
