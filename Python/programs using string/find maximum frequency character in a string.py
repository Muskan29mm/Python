def max_frequency_character(s):
    frequency = {}

    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    max_freq = float('-1')
    max_freq_character = None

    for char, freq in frequency.items():
        if freq > max_freq:
            max_freq = freq
            max_freq_character = char

    return max_freq_character

input_string = "National Animal of India is bengal Tiger"
result = max_frequency_character(input_string)
print(f"The Maximum frequent character is: '{result}'")

# in output it will also consider space and space has max_frequecy_character that's why it is showing blank output