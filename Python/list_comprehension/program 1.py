# Python list_comprehension

fruits = ["Apple", "Banana", "Cherry", "Mango", "papaya", "pineapple", "kiwi"]

new_list = [x for x in fruits if "a" in x]
print(new_list)

# With condition
new_list1 = [x for x in fruits if x!= "Apple"]
print(new_list1)

# Iterable
new_list2 = [x for x in range(10)]
print(new_list2)

# Iterable with condition
new_list3 = [x for x in range(10) if x > 5]
print(new_list3)

# Expression
new_list4 = [x.upper() for x in fruits]
print(new_list4)

# Return "orange" instead of "banana"
new_list5 = [x if x != "Banana" else "orange" for x in fruits]
print(new_list5)
