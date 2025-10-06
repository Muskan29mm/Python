# Python Arrays

fruits = ["Apple", "Banana", "Cherry"]
print(fruits)

# Access elements of array
x = fruits[1]
print(x)

# Modify the value of first array item
fruits[1] = "Mango"
print(fruits)

# To find length of an array
a = len(fruits)
print(a)

# Looping array elements
for y in fruits:
    print(y)

# Add array element ( use append() method )
fruits.append("Kiwi")
print(fruits)

# Removing array elements ( use pop() method)
fruits.pop(3)
print(fruits)

# You can also use remove() method to remove an element of an array
fruits.remove("Apple")
print(fruits)

# copy() method
z = fruits.copy()
print(z)

# count() method. The count() method returns the number of elements with the specified value
b = fruits.count('Mango')
print(b)

# extend() method
# extend() method adds the specified list elements (or any iterable) to the end of the current list.
fruits1 = ["Kiwi", "Banana", "Grapes"]
fruits.extend(fruits1)
print(fruits)

# insert() method
# insert method insert the item at specified index
fruits.insert(2, "Orange")
print(fruits)

# reverse() method
fruits.reverse()
print(fruits)

# sort() method
fruits.sort()
print(fruits)

# Slicing python arrays
print(fruits[2:4])
