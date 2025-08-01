# Add Items to set

# Once the set is created you cannot change it's item, but you can add new items

# use "add" method to add items
thisset = {"apple", "banana", "cherry"}
print(thisset)
thisset.add("Mango")
print(thisset)

# To add items from oen set to another set use "update" method
set1 = {"apple", "mango", "banana"}
set2 = {"cherry", "peach", "grapes"}
print(set1)
print(set2)
set1.update(set2)
print(set1)

# Add Any Iterable(list, tuple, dict)
set3 = {"apple", "mango", "banana"}
mylist = ["cherry", "pineapple", "grapes"]
mytuple = ("plum", "peach", "melon")
#set3.update(mytuple)
set3.update(mylist)
print(set3)