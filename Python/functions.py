def my_function():
    print("Hello world")

my_function()

# with arguments
def my_functions(fname):
    print(fname + " Ref")


my_functions("Emil")
my_functions("Joe")

# if you don't know how many functions are to be passed to your function, used * symbol
def my_function1(*fname):
    print("The name is " + fname[1])

my_function1("Emil", "Joe", "Linus")

# function can't be empty if you don't have any value to return by a function use "pass" keyword
def my_name():
    pass

# passing a list as argument
def list(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]
list(fruits)
