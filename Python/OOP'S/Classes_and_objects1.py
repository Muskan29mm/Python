# Another script for classes and objects
from Python.Functions import myFunc


# create a class and object
class Dog:
    species = "Canine" # class attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age


# create an object
dog1 = Dog("Buddy", 3)
print(dog1.name) # instance attribute
print(dog1.age)  # instance attribute
print(dog1.species) # class attribute

print()

# the __str__ method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"

p1 = Person("John", 23)

print(p1.name)
print(p1.age)
print(p1)

print()

# Create methods
class Person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p2 = Person1("Joe", 12)
print(p2.name)
p2.myfunc()

print()

# Self parameter
class FG:
    define = "Fruits"   # class attribute

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f"{self.name} is {self.color}"

f1 = FG("Apple", "Red")
print(f1)  # calls __str__
print(f1.name, f1.color)

print()

# Modify object properties
class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is :" + self.name)


p3 = Person2("Jack", 34)

print(p3.name)
print(p3.age)

# modify the age
p3.age = 37

print(p3.age)

# pass statement
class Person3:
    pass


# delete object properties (using del keyword)
# del p3.age
# print(p3.age)  # it will throw an error because object property  is deleted
#
# # delete object
# del p3
# print(p3)