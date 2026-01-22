# Program to remove duplicate from a string

string1 = input("Enter a string:")

rem =""

for char in string1:
    if char not in rem:
        rem = rem + char
print("String after removing duplicate characters:", rem)