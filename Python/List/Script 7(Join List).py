# Join a list

# join two lists
list1 =["a", "b", "c"]
list2 = [2, 4, 6]
list3 = list1 + list2
print(list3)

# by appending all items from list2 to list1
list1 = ["d", "e", "f"]
list2 = [3, 4, 5]

for x in list2:
    list1.append(x)
print(list1)

# Use extend() method
list5 = ["g", "h", "k"]
list6 = [6, 7, 9]

list5.extend(list6)
print(list5)