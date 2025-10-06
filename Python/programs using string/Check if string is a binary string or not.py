# Python program to check if string is a binary string or not

a = input("Enter the string: ").strip()

if all(char in '01' for char in a) and a:
    print(a,"is a binary string")
else:
    print(a,"is not a binary string")

