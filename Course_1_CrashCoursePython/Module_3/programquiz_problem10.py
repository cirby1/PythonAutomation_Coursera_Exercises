def test_code(num):
    x = num
    while x % 2 == 0:
        x = x / 2

print(test_code(10))

#Missing an else statement. But there's no if statement.
#When called with a 0 makes sense. But the while loop is funky.
#The Modulo operator is used incorrectly. I don't think it is. You can continue looping while the variable is even..
#Missing the continue keyword? That's for breaking out of something. 

#I think it's called with a 0, It triggers an infinite loop. 
