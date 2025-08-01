# Remove Items from a set

thisset = {"apple", "banana", "cherry"}
print(thisset)
thisset.remove("banana")
print(thisset)

# Remove banana by using "discard" method
set1 = {"Apple", "Mango", "Banana", "Cherry"}
print(set1)
set1.discard("Banana")
print(set1)

# You can use "pop" method also, but this method will remove any random item, so you cannot be sure what item that gets removed
set2 = {"apple", "banana", "orange", "mango", "watermelon"}
print(set2)
x = set2.pop()
print(x) #removed item
print(set2)

# The "clear" method empties the set
set3 = {"Mango", "Apple", "Cherry", "Banana"}
print(set3)
set3.clear()
print(set3)

# To delete the whole set
set4 =  {"apple", "mango", "banana", "cherry"}
print(set4)
del set4
print(set4)
