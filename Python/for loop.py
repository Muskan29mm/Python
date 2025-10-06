# For loop in python

# Print each fruit in fruits list

fruits = ["Apple", "Mango", "Banana"]
for x in fruits:
    print(x)

# Add a newline to separate outputs of the two loops
print()

# Looping through strings
for x in "Mango":
    print(x)

# Add a newline to separate outputs of the two loops
print()

# using "break" statement (using break we can stop the loop before iterating whole item)
fruits1 = ["Apple", "Mango", "Banana", "cherry"]
for x in fruits1:
    print(x)
    if x == "Banana":
        break

# Add a newline to separate outputs of the two loops
print()

# Exit the loop when x is "banana", but this time the break comes before the print
for x in fruits1:
    if x == "Mango":
        break
    print(x)

print()

# Continue statement (In continue statement we can stop the current iteration of the loop, and continue with the next)
fruits2 = ["Cheery", "Banana", "Pineapple", "Apple"]
for x in fruits2:
    if x == "Banana":
        continue
    print(x)

print()

# range function
for x in range(6):
    print(x)

print()

# The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6)
for x in range(2, 6):
    print(x)

print()

# range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3)
for y in range(2, 15, 2):
    print(y)

print()

# else in for loop
for x in range(6):
    print(x)
else:
    print("Finished loop")

print()

# The else block will NOT be executed if the loop is stopped by a break statement
for z in range(7):
    if z == 5:
        break
    print(z)
else:
    print("Finally Finished")

# Print each adjective for every fruit
adj = ["red", "big", "tasty"]
fruits = ["apple", "plum", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

# pass statement
for x in [1, 2, 3]:
    pass