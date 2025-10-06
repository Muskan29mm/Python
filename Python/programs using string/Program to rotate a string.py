# Python program to rotate a string using slicing

string = "This is Pycharm"
n = 7  # Number of Positions to rotate
a = string[-n:] + string[:-n]


print(a)
