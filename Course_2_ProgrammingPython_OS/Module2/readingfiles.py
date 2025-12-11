#So this is two ways of doing the same thing.
file = open("spider.txt")
print(file.readline())
print(file.readline())
print(file.readline())

print(file.read())
file.close()

with open("spider.txt") as file:
	print(file.readline())


#I always need to close out the file after opening it. The with command does it once it is done. 
