#4 Which list method can be used to add a new element to a list at a specified index position?
mylist = ["red", "yell", "blu", "whi"]
print(mylist)

result = mylist.pop(0)
print(result)
print()

#This one actually worked.
result = mylist.insert(1, "stuff")
print(mylist)

#This one doesn't work...
#result = mylist.add(1, "stuffy")
#print(mylist)

#This one only appends to the end.
result = mylist.append("stufffff")
print(mylist)

#The correct answer is B the insert method.
