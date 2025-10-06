# Python program to remove all duplicates from dictoonary

string = 'Python is great and Java is also great'

print(' '.join(dict.fromkeys(string.split())))

# explanation
# string.split(): This method splits the string into a list of words.
# The default delimiter is whitespace, so the string is split at each space.

# dict.fromkeys(...): This method creates a new dictionary where the keys are the elements from the provided iterable
# (in this case, the list of words from the string.split()), and all values are set to None by default.
# This effectively removes duplicate keys because dictionary keys are unique.
# After applying dict.fromkeys, you get a dictionary where each word is a key and duplicate keys are removed.