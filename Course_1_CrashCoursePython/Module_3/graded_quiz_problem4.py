#By adding the start/stop variables to the for loop and going +1, it made it all work good. 

def multiplication_table(start, stop):
    #Complete the outer loop range.
    for x in range(start, stop+1):
        for y in range(start, stop+1):
            print(str(x*y), end=" ")    
        print()

multiplication_table(1,3)



