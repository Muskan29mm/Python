class MyClass:
    x = 5

# to create object
p1 = MyClass()
print(p1.x)

# init function
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p2 = Person("john", 34)

print(p2.name)
print(p2.age)
