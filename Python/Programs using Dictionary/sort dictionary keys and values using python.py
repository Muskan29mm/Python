# Python program to sort dictionary keys and values

dict1 = {'a':3, 'z':7, 'l':1, 'r':9, 'e':0}

# In this we have sorted the dictionary using key
myKeys = list(dict1.keys())
myKeys.sort()
sorted_dict = {i: dict1[i] for i in myKeys}

print("The Sorted Dictionary by key is :",sorted_dict)

# In this we have sorted the dictionary using values
myValues = sorted(dict1.items(), key=lambda item: item[1])
sorted_dict1 = dict(myValues)
print("The sorted Dictionary by values is :",sorted_dict1)