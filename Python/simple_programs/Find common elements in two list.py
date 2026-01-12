# Find common elements in two lists

list1 = [1,3,5,7,9]
list2 = [0,3,1,4,0,6,7]

a = set(list1)
b = set(list2)
common_elements = a.intersection(b)

print("Common elements:", common_elements)