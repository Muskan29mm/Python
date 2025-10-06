# Python program to check if string is palindrome or not

import re

def is_palindrome(s):
    # Normalize the string: lower case and remove non-alphanumeric characters
    normalized_string = re.sub(r'[^A-Za-z0-9]', '', s).lower()
    return normalized_string == normalized_string[::-1]

a = input("Enter the string: ")
if is_palindrome(a):
    print(a, "is a palindrome")
else:
    print(a, "is not a palindrome")
