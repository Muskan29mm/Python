# Check palindrome number or string

def is_palindrome(input_data):
    str_data = str(input_data)
    return str_data == str_data[::-1]



input_value = "madam" # Level, racecar, 

if is_palindrome(input_value):
    print(f"{input_value} is a palindrome")

else:
    print(f"{input_value} is not a palindrome")