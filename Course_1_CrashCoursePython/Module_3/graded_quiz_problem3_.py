#Okay I think I got it. I would need to int or floor the decimal whenever I am dividing by 10.
def digits(n):
    count = 0
    if n == 0:
        count += 1
    while n > 0:
        count +=1
        n = int(n/10)
    return count

print(digits(1555))
