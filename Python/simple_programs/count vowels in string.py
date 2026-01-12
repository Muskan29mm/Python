# Count vowels in string

def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count
    
input_str = "Hello! HOw are you?"

vowel_count = count_vowels(input_str)
print("Number of vowels:", vowel_count)