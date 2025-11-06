#Write a function that takes an argument n and returns the sum of integers from 1 to n. For example, if n=5 your function should add up 1+2+3+4+5 and return 15. If n is less than 1, just return 0. Use a while loop to calculate this sum.

def sum_of_integers(n):
    x = 0
    collection = 0
    while x < n:
        if n < 1:
            print("The number is lower")
            return 0
        x = x + 1
        collection = collection + x
    return collection
    print("The collected amount is: " + str(collection))
    
print(sum_of_integers(6))


