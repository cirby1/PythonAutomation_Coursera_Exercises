"""
Methods are basically actions that your classes or objects do. I like to think of an action figure. The actions only work on that specific action figure, not all the action figures that you have. So to speak. They only work locally and not globally.

Methods fall into these categories:

    -Instance Methods

    -Class Methods

    -Static Methods

-Instance Methods are basically personal self actions for a single action figure. In Python terms they mean the methods that are within a class. Instance methods can take this keyword called "Self" and access different parts of the class or object. For example, using "self.name" to access the name of the object. I think another part of it is that these instances are copies of the main original class. So you can do things with the copies like call methods. 

-Class Methods are used for the class itself and not any of the instances. I'm guessing these are some of the master blueprint methods for the class.

-Static Methods behave like plain functions, except you can call them directly from the class. 

A good way of looking at it is: 
    -Instance Methods use "me" the object - Needs the "self" keyword.
    -Class Methods use "us" the class - Needs "cls", this action depends on all of us as a category.
    -Static Method uses nobody, no "self" keyword and no "cls" keyword. 


The type of method you choose to use whether it's instance, class, or static depends on the type of data you need to access. These are all different tools in the toolbox depending on the situation. 

-Instance Methods are for individual object data.
-For alternative constructors or class settings.
-Utility or helper function just stored inside of the class just in case. 
"""
