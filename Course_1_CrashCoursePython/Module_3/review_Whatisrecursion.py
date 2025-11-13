"""
def factorial(inserted_number):
    if inserted_number < 2:
        return 1
    return inserted_number * factorial(inserted_number-1)
"""


#Every layer is frozen since you are returning something
#For example, if the inserted number is 5, then:
    #Return 5 * factorial(5 - 1)
                #Return 5 * factorial(4 - 1)
                            #Return 5 * factorial(3 - 1)
                                        #Return 5 * factorial(2 - 1)
                                                    #Return 5 * factorial(1)
                                                                #return 1
    #5 * 5 * 5 * 5 * 5 * 1
    #25 *    5 * 5 * 5 * 1
    #25 *    5 * 5 * 5
    #125       * 5 * 5
    #3125

#OH! I messed up... I didn't subtract on the first line. So:
# 5 * 4 * 3 * 2 * 1

#print(5*4*3*2*1)


def factorial(n):
    print("Factorial called with " + str(n))
    if n < 2:
        print("Returning 1")
        return 1
    result = n * factorial(n-1)
    print("Returning " + str(result) + " for factorial of " + str(n))
    return result

factorial(4)

#4 * 3 * 2 * 1 = 24























