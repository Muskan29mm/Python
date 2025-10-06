# Python Functions

# creating and calling a function
def func():
    print("Hello World!")

func()

# function with arguments ( we will create a function to check if the number is even or odd )
def evenOdd(x):
    if (x % 2 == 0):
        return "Even"
    else:
        return "Odd"

print(evenOdd(12))
print(evenOdd(3))


# Types of arguments
# 1. Default arguments
def myFunc(x, y=10):
    print("value of x is: ", x)
    print("value of y is: ", y)

myFunc(2)

# 2. Keyword arguments
def Func1(fname, lname):
    print(fname, lname)

Func1(fname='Hello', lname='World')
Func1(lname='World', fname='Hello')

# 3. Positional arguments
def nameAge(name, age):
    print("Hi, I am", name)
    print("I am", age)

nameAge("Joe", 23)

# 4. Arbitrary keyword argument
# There are two arbitrary keyword arguments(args(non-keyword arguments, kwargs(keyword arguments))
# ex - args arguments
def myFunc2(*args):
    for arg in args:
        print(arg)

myFunc2('Hello', 'World')

# ex- kwargs arguments
def myFunc3(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value) )

myFunc3(first='Hello', last='Joe')


# return statement in functions
def square_value(num):
    return num**2

print(square_value(4))

# Pass By reference
def addItem(myList):
    myList.append(12)

numbers = [10,20,30,40]
addItem(numbers)
print(numbers)

# Pass by value (Changes are done locally only i.e inside the function)
def add_one(n):
    n += 1
    print(n)

x = 5
add_one(x)
print(x)

print()

# recursion
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

# Another example fo (*args and **kwargs)
def show_details(*args, **kwargs):
    print("Arguments (args):", args)
    print("Keyword Arguments (kwargs):", kwargs)

show_details(10, 20, name="Muskan", age=25, gender="Female")
