# Python program to extract unique values from a dictionary
data_dict = {
    'gfg': [5, 6, 7, 8],
    'is': [10, 11, 7, 5],
    'best': [6, 12, 10, 8],
    'for': [1, 2, 5]
}

# Initialize an empty set to collect unique values
unique_values = set()

for value_list in data_dict.values():
    for value in value_list:
        # Check if the value is an integer (or numeric) and add to the set
        if isinstance(value, int):
            unique_values.add(value)

unique_values_list = sorted(unique_values)

print("Unique values list is:", unique_values_list)
