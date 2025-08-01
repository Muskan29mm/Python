# Remove List Items

# Use "remove" method to remove item from list
thislist = ["Apple", "Banana", "Cherry"]
print(thislist)
thislist.remove("Banana")
print(thislist)

# If there are more than one item with the specified value, the remove method removes the first occurrence
thislist1 = ["Apple", "Banana", "Cherry", "Apple"]
thislist1.remove("Apple")
print(thislist1)

# Remove at specified index using 'pop' method
thislist2 = ["Apple", "Banana", "Cherry", "Mango"]
thislist2.pop(1)
print(thislist2)

# If you don't specify the index the pop will remove the last element
thislist2.pop()
print(thislist2)

# 'del' keyword also removes at specified index
thislist3 = ["Pineapple", "Orange", "Grapes"]
print(thislist3)
del thislist3[1]
print(thislist3)

# Clear the list
# This empties the list. List will be there but with no content
thislist5 = ["Apple", "Banana", "Cherry"]
print(thislist5)
thislist5.clear()
print(thislist5)

# 'del' keyword can also remove the list completely
# It will throw an error becuase list is deleted
thislist4 = ["Apple", "Banana", "Cherry"]
print(thislist4)
del thislist4
print(thislist4)

