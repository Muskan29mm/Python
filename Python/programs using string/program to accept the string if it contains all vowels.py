# Python program to accept the string if it contains all vowels

string = input("Enter the String")

vowels = 'aeiou'

if vowels in string:
    print("The string contains all vowels")
    print("The String is ", string)
else:
    print("The string doesnot contain all vowels")