# Python program to check if string contains any special character

string = "Python is_a Programming_Language"

special_characters = "[@_!#$%^&*()<>?/\|}{~:]"

contains_special = False

for char in special_characters:
    if char in string:
        contains_special = True
        break

if contains_special:
    print("String is not accepted")
else:
    print("String is accepted")
    print(string)
