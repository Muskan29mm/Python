# Types of decorators

# 1. Function decorators
print("------------------FUNCTION DECORATOR------------------------")
def decorator(func):
    def wrapper():
        print("Before calling the function")
        func()
        print("After calling the function")
    return wrapper

@decorator
def greet():
    print("Hello world!")

greet()

print()

# 2. Method Decorator
print("------------------METHOD DECORATOR---------------------------")
def method_decorator(func):
    def wrapper(self, *args, **kwargs):
        print("Before method execution")
        res = func(self, *args, **kwargs)
        print("After calling execution")
        return res
    return wrapper

class MyClass:
    @method_decorator
    def say_hello(self):
        print("Hello!")

obj = MyClass()
obj.say_hello()

print()

# 3. Class Decorator
print("------------------CLASS DECORATOR-----------------------------")
def func(cls):
    cls.class_name = cls.__name__         # The value of the class_name is set to the name of the class
    return cls

@func
class Person:
    pass

print(Person.class_name)