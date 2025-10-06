# Decorators in python

# Here in this example "decorator" function takes the "greet" function as an argument
def decorator(func):
    def wrapper():
        print("Before calling the function")
        func()
        print("After calling the function")

    return wrapper

@decorator
def greet():
    print("Hello, World!")

greet()

