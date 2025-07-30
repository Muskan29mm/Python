# List

thislist = ["apple", "banana", "cheery"]
print(thislist)

# Allow Duplicates
list1 = ["apple", "banana", "cherry", "apple", "mango"]
print(list1)

# To determine the length of a list
print(len(list1))

# List can be of any datatype
list2 = [1,2,4,6]
list3 = [True, False, True, False]
print(list2)
print(list3)

# List can contain different datatype
list4 = ["Apple", 4, "Banana", True, 0]
print(list4)

# type()
print(type(list4))

# list() constructor
list5 = list(("Apple", "banana", "cherry", "mango"))
print(list5)

# Access List Items
print(list5[1])

# Negative indexing
print(list5[-2])

# Range of Indexes
list6 = ["apple", "banana", "cherry", "mango", "pineapple", "orange", "strawberry"]
print(list6[2:5])

# Leaving out start value range will start at First item
list7 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(list7[:4])

# Leaving out the end value range will go on to the end of the list
print(list7[4:])

# Range of Negative indexes
print(list7[-4:-1])

# Check if item exists
if "apple" in list7:
    print("'Yes', apple is in list ")