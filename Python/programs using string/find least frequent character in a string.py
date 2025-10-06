# Program to find least frequent character in a string
def least_frequent_character(s):
    # Dictionary to store frequency of each character
    frequency = {}

    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    min_freq = float('inf')  # Initialize to a large number
    least_freq_char = None

    for char, freq in frequency.items():
        if freq < min_freq:
            min_freq = freq
            least_freq_char = char

    return least_freq_char

input_string = "National Animal of India is bengal Tiger"
result = least_frequent_character(input_string)
print(f"The least frequent character is: '{result}'")
