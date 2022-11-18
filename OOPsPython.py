# Class is a user defined prototypes. It has Methods, Class variables, instances, constructors.
# Object is an instance of class. And they are created outside of Class.
# We can have "n" number of objects for a class but vice versa  is NOT possible.
# Constructor is method which is called automatically when an object is created.
# Class variables are defined inside class
# Instance variables are defined under constructors
# Self is a default object and is mandatory to call instance variables.
# Class variables can be called using classname. or self.

class Parent:
    a = 20  # Class Variable

    def __init__(self, a, b):  # Default Constructor
        print("Default Constructor")
        self.FirstNumber = a
        self.SecondNumber = b

    def addition(self):
        return self.FirstNumber + self.SecondNumber + Parent.a


obj = Parent(10, 20)  # Syntax to create an object of a class.
print(obj.addition())

obj1 = Parent(30, 40)
print(obj1.addition())
