# Add List Items

# Append Items using 'append' method
thislist = ["Apple", "Banana", "Cherry"]
print(thislist)
thislist.append("Mango")
print(thislist)

# Insert Items at specified index use 'insert' method
thislist1 = ["apple", "banana", "cherry"]
print(thislist1)
thislist1.insert(2, "Mango")
print(thislist1)

# To insert elements from another list use "extend" method
thislist2 = ["apple", "banana", "cherry"]
tropical = ["pineapple", "mango", "blueberry"]
thislist2.extend(tropical)
print(thislist2)

# Add any Iterable (The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.))
thislist3 = ["Apple", "Banana", "Cherry"]
thistuple = ("Mango", "Peach", "Plum")
thislist3.extend(thistuple)
print(thislist3)

# If we append dictionary
thisdict = {'Mango', 'Pineapple', 'Raspberry'}
thislist3.extend(thisdict)
print(thislist3)