"""
Create a multiplication Table that prints out this:

if the call is multiplication_table(3)

#3x1=3
#3x2=6
#3x3=9
#3x4=12
#3x5=15
"""
def times_table(n):
    primary_number = n
    cycler_number = 1
    multiplication_result = 0

    while cycler_number <= 5:
        multiplication_result = primary_number * cycler_number
        print(str(primary_number) + "x" + str(cycler_number) + "=" + str(multiplication_result))
        cycler_number += 1

times_table(3)
times_table(5)
times_table(8)
    
