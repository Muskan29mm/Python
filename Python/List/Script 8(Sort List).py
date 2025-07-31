# Sort the list

# Sort list alphanumerically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# Sort the list numerically
thislist1 = [100, 50, 65, 82, 23]
thislist1.sort()
print(thislist1)

# Sort Descending
thislist3 = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist3.sort(reverse=True)
print(thislist3)

# Sort the numerical list descending
thislist4 = [100, 50, 65, 82, 23]
thislist4.sort(reverse=True)
print(thislist4)

# Customize sort function
def myfunc(n):
    return abs(n - 50)

thislist5 = [100, 50, 65, 82, 23]
thislist5.sort(key = myfunc)
print(thislist5)

# Case Insensitive Sort
# By default it sort first Upper case letter first then lower case letter
thislist6 = ["banana", "Orange", "Kiwi", "cherry"]
thislist6.sort()
print(thislist6)

# To sort lower case letter first, use str.lower as a key function
thislist7 = ["banana", "Orange", "Kiwi", "cherry"]
thislist7.sort(key = str.lower)
print(thislist7)

# Reverse Order
thislist8 = ["banana", "Orange", "Kiwi", "cherry"]
thislist8.reverse()
print(thislist8)