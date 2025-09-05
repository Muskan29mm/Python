# Run time polymorphism (Method overriding)
# Child class provides it's own version of a method defined in the parent class
# Python decides at run time which method to call based on the object type

class Animal:
    def sound(self):
        return "Some generic sound"


class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

animal = [Dog(), Cat(), Animal()]
for animals in animal:
    print(animals.sound())

# Here sound method behaves differently depending on whether object is a Dog, Cat or Animal and this decision happens at runtime