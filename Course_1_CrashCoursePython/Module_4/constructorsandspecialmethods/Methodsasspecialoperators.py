"""
Methods as special operators

You have already learned about methods and how they are just functions that belong to a class. They define the behavior that an object of the class can perform. Special operators are specific symbols or keywords taht are built-in and provide special behavior when used with certain data types of objects. In your class, you can define methods to implement or override the standard behavior of Python operators, thus creating methods as special operators. 

In this reading you will learn about the different types of special operators, how to override the standard operators and embed them in your code, and see examples along the way. 

Different types of special operators

Python supports a variety of different operators that you can use in your code to make life easier for you. Some of the more common operators are:

    -Arithmetic operators like + addition, - subtraction, * multiplication, / division, and ** exponents.

    -Comparison operators include == equality, != inequality, < less than, >= greater than or equal to.

    -Logical operators like and, or, and not. 

*There's more and this isn't of course a complete list.*
"""

"""
Performing special operations

Every special operator has a corresponding dunder method that implements the operation. In Python, you denote a dunder method by placing double underscores at the beginning and end of the name, in fact, the term "dunder" comes from this use of double underscores. You can change how an operator behaves with an instance of your object by overriding the implmentation. Let's look at an example:
"""

class Square:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    #As you can see the numbers that get "plugged in" within the parentheses go down to the length and the width. 
    #And we can make an area method which multiplies these two numbers together.

    def area(self):
        return self.length * self.width

mybox = Square(10, 20)
print(mybox.area())



