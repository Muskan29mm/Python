# Python program to find sum of all values in a dictionary

dict1 = {'a': 3, 'b': 4, 'c': 5, 'd': 9, 'e': 2, 'f': 1}

v1 = list(dict1.values())
print(v1)


value_list = []
for i in dict1:
    value_list.append(dict1[i])
total = sum(value_list)

print(total)


