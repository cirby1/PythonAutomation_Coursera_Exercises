#3 If we have a string variable named Weather = "Rainfall", which of the following will print the substring "Rain" or all characters before the "f"?

Weather = "Rainfall"
#print(Weather[0:4]) this one prints Rain
#print(Weather[4:]) this one prints fall
#print(Weather[1:4]) this one prints ain
print(Weather[:"f"]) #This one throws an error and doesn't work. 
