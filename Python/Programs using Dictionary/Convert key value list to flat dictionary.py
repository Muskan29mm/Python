# Program to convert key value list to flat dictionary

from itertools import product

test_dict = {'month' : [1, 2, 3],
             'name' : ['Jan', 'Feb', 'March']}

print("The original dictionary is : " + str(test_dict))

# Convert key values list to flat dictionary
res = dict(zip(test_dict['month'], test_dict['name']))

print("The Flatten Dictionary is : " + str(res))