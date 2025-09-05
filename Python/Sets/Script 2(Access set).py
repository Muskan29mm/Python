# Access set

# You cannot access set items by using index or key, but you can loop through set items
set1 = {"apple", "banana", "cherry"}
for x in set1:
    print(x)

# Check if "banana" is present in the set
if "banana" in set1:
    print("yes, 'banana' is in set1")

# Check if "banana" is NOT present in the set
thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset)
