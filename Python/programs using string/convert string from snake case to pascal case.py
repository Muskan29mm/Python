# Python program to convert snake case to pascal case
def snake_to_pascal(snake_str):
    words = snake_str.split('_')
    pascal_str = ''.join(word.capitalize() for word in words)
    return pascal_str

snake_case_string = 'this_is_a_snake_case_string'
pascal_case_string = snake_to_pascal(snake_case_string)
print(pascal_case_string)
