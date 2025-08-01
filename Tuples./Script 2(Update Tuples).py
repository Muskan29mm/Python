# To update Tuple

# As tuple is unchangeable you cannot change tuple value but there is workaround you can convert tuple to list change it's value and convert back to tuple
# Change Tuple value
thistuple = ("apple", "banana", "Cherry")
print(thistuple)
X = list(thistuple)
print(X)
X[2] = "Kiwi" # change value
print(X)
Y = tuple(X)
print(Y)

# Add Items
# To add items to a tuple, convert it into a list and convert back to tuple
# In this tuple is already converted to a list and stored in X variable. append new item to a list and convert that into a tuple and stored in new variable i.e Z
X.append("Orange")
print(X)
Z = tuple(X)
print(Z)

# Add tuple to tuple
M = ('Mango',)
Z += M
print(Z)

# To delete Items
# To delete items from a tuple, convert it into a list and after deleting convert back to tuple
U = list(Z)
print(U)
W = U.remove("Mango")
print(W)  # Because there is nothing in W so it will print None
print(U)
T = tuple(U)
print(T)


# To delete whole tuple use 'del' keyword
del T
print(T)   # This will raise an error because tuple no longer exists
