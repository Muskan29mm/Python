# Find duplicate characters in a string

def find_duplicate_characters(input_string):
    char_count = {}
    duplicates = []

    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char, count in char_count.items():
        if count > 1:
            duplicates.append(char)
    return duplicates

input_str = "object oriented programming"
duplicate_chars = find_duplicate_characters(input_str)
print("Duplicate characters:", duplicate_chars)