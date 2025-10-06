# Program to remove the ith index from the given string

string = input("Enter the String:")

index = int(input("Enter the index Number to remove:"))

if 0 <= index < len(string):
    new_string = string[:index] + string[index + 1:]
    print(new_string)

