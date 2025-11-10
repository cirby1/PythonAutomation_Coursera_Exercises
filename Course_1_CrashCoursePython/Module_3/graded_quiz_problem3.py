luckynumber = 25
CanItDivideBy10 = (luckynumber % 10 != 0)
print(CanItDivideBy10)
#We need to check checking until the number is depleted. 
#Cycle until the number is over.
    #Check can 10 go into it?
        #If so then keep tabs and subtract 10.
        #If not then we are done and it's just a single digit number. 
keepingcount = 0
while luckynumber > 0:
    if luckynumber < 0:
        break
    if (luckynumber / 10 != 0) & (luckynumber - 10 > 0):
        keepingcount += 1 #This means that the digit can be divided and so we keep count of the 1st digit.
        print(str(luckynumber) + " " +"The Lucky Number can be further divided by 10")
        luckynumber = int(luckynumber / 10)
    else:
        keepingcount += 1
        print(str(luckynumber) + "" + "The Lucky Number is now a single digit.")
        break
print("Outside of the while loop.")
print("The count was " + str(keepingcount))













