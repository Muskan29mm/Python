# Program to find number of matching characters in two strings

def common(str1,str2):
    return(len((set(str1)).intersection(set(str2))))

a = input("Enter the string 1:")
b = input("Enter the string 2:")

commom_characters = common(a,b)

print("The numbers of common characters in both string are:",commom_characters)


# output check if character exists in string 2 if yes then count = 1 else count = 0 and if one of the string has more charcaters than
# other string it will count that too