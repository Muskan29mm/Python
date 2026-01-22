# Program to remove space from string

string1 = input("Enter a string: ")

rem = string1.strip()
print("String after removing leading and trailing spaces:", rem)
rem1 = string1.replace(" ", "")
print("String after removing all spaces:", rem1)