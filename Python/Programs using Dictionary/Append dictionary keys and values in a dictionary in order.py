# Python program to append dictionary keys and values in a dictionary in order

dict1 = {'a': 1, 'b':2, 'c':3, 'd':4}

output_dict = list(dict1.keys()) + list(dict1.values())

print("The original Dictionary is :", dict1)

print("The Dictionary after appending dictionary keys and values in order is :", output_dict)

