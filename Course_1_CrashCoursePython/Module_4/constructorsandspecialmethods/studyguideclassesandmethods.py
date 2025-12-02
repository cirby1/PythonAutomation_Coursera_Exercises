"""
Study Guide: Classes and Methods

In the past, we have seend how to define classes and methods in Python. Here is a run down of everything that you has been covered. Here is defining classes and methods. 

class ClassName:
    def method_name(self, other_parameters):
        body_of_method
"""


"""
Classes and Instances

-Classes define the behavior of all instances of a specific class. In Python, the code defining a class is, itself, an object; classes can be used without instantiating a single object, such as when using static methods. 

-Remember, each variable of a specific class is an instance or object.

-In Python, "getters and setters", are methods used for controlling access to an object's attributes. The getter method retrieves the value of an attribute, while the setter method sets or changes the attributes value, often including some sort of validation or modification to the data before setting the value. 

-You can access an instance's  attribute, like name, by calling self.name within the class methods, or <instance> is the specific instance of the class you're working with. Objects can have attributes, which store information about the object.

-You can make objects do work by calling their methods. 

-The first parameter of the methods, (self), represents the current instance.

-Methods are just like function, but they can nly be used through a class.

-You can use class methods in conjunctin with a class variable to track the nmber of instances of a class, incremementing the class variable each time an instance is created in the class's __init__ method. 

"""
Special Methods

-Special Methods start and end with __.

-Special methods have specific names, like __init__ for the constructor or __str___ for the conversion to string.

-The methods __str__ and repr__ allow you to define human-readable and unambiguous string representations of your objects, respectively.

-By defining methods like __eq__, __ne__, __lt__, __gt__, __le__, and __ge__, you can control how objects of your class are compared. 
"""

"""
Documenting classes, methods, and functions.
-You can add documentation to classe, methods, and function by using docstrings right after the definition. Like this:
"""

class ClassName:
    """Documentation for the class."""
    def method_name(self, other_parameters):
        """Documentation for the method."""
        body_of_method

    def function_name(parameters):
        """Documentation for the function."""
        body_of_functin

"""
A great way to use docstrings is to have an example of using the function, with its expected output.
"""

def my_function(x):
    """
    Sample usage:
    >>> my_function("example input")
    "example output"
    """

#When in interactive Python, you can display docstrongs with:
help(some_function)


#Or in your code you can retrieve it and use it in your program just as you would with any other string.
some_function.__doc__
print(some_function.__doc__)
function_explanation = other_function.__doc__




