#CodingSkills 3 Part 2
#Use a list comprehension [] with a for loop and an if condition. 

firstnumber = 1
lastnumber = 25

result = [individual_number for individual_number in range(firstnumber, lastnumber) if individual_number % 5 == 0]
print(result)

#Okay, I kind of understand this. Let's see If I can do somemore.

lowest_buyprice = 100
highest_buyprice = 200

N64Prices = [price for price in range(lowest_buyprice, highest_buyprice) if price % 10 == 0]
print(N64Prices)

XboxPrices = [price for price in range(150, highest_buyprice) if price % 2 != 0]
print(XboxPrices)

#Okay, I think I understand. Moving onto Coding Skill 4 now...
