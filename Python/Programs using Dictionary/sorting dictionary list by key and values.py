# Python program to sort the dictionary list by key and values

test_dict = {'gfg': [7, 6, 3],
             'is': [2, 10, 3],
             'best': [19, 4]}

print("The original dictionary is : " + str(test_dict))

res = dict()
for key in sorted(test_dict):   # this line sorts the keys of test_dict in ascending order and uses for loop to process each key in sorted order
    res[key] = sorted(test_dict[key])   # this line sets the value in the res dictionary after sorting from original value that is associated with that key in test_dict

print("The sorted dictionary is : " + str(res))

