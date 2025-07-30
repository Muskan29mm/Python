# Tuples

# Create a tuple
tuple1 = ("Banana", "Apple", "Cherry")
print(tuple1)

# Since tuples allow duplicates
tuple2 = ("Banana", "Cherry", "Apple", "Orange", "Apple")
print(tuple2)

# to determine tuple length
tuple3 = ("Banana", "Apple", "Cherry", "Mango", "Orange")
print(len(tuple3))

# Create tuple with one item
tuple4 = ("Banana",)
print(tuple4)

# Tuple item can contain different datatypes
tuple5 = ("Banana", 7, "Cherry", True, 3.67)
print(tuple5)

# To find type of tuple
tuple6 = ("Banana", "Apple", "Cherry")
print(type(tuple6))

# To make tuple constructor using tuple() constructor to make a tuple
tuple7 = tuple(("Banana", "Apple", "Cherry", "Mango"))
print(tuple7)

# Access Tuple items
print(tuple7[1])

# Access Tuple items using negative indexing (To access last item)
print(tuple7[-1])

# Access tuple items using range of indexes
tuple8 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(tuple8[2:5])

# Leaving the start value
print(tuple8[:4])

# Leaving the end value
print(tuple8[4:])

# Range of Negative indexing (last item will be excluded)
print(tuple8[-4:-1])

# Check if "Item" exits
if "cherry" in tuple8:
    print("Cherry exits in tuple 8")

