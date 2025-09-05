# Join sets
# There are several ways to join a sets

# Union() method
set1 = {"apple", "banana", "cherry"}
set2 = {"mango", "guava", "pineapple"}
set3 = set1.union(set2)
print(set3)

# You can use the | operator instead of the union() method, and you will get the same result.
set4 = set1 | set2
print(set4)

# Join Multiple sets
set5 = {"apple", "banana", "mango"}
set6 = {7, 9, 6}
set7 = {"a", "b", "c"}
set8 = {"john", "sam"}
set9 = set5.union(set6, set7, set8)
print(set9)

# When using the | operator, separate the sets with more | operators
a = set5 | set6 | set7 | set8
print(a)

# Join a set and a tuple
set10 = {"apple", "mango", "kiwi"}
tuple1 = ("a", "b", "c")
b = set10.union(tuple1)
print(b)

# Union() method also removes duplicates
set11 = {"a", "b", "c"}
set12 = {"c", "d", "e"}
c = set11.union(set12)
print(c)

# Update() method
set13 = {"f", "g", "h"}
set14 = {1, 2, 3}
set13.update(set14)
print(set13)

# Intersection (It will return only those item that are present in both the sets)
set15 = {"apple", "kiwi", "cherry", "pineapple"}
set16 = {"orange", "apple", "grapes", "plum", "kiwi"}
d = set15.intersection(set16)
print(d)

# You can use the & operator instead of the intersection() method, and you will get the same result
set17 = {"apple", "banana", "cherry"}
set18 = {"mango", "orange", "apple"}
e = set17 & set18
print(e)

# intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set
set19 = {"apple", "banana", "cherry"}
set20 = {"banana", "kiwi", "apple"}
print(set19)
print(set20)
set19.intersection_update(set20)
print(set19)

# The values True and 1 are considered the same value. The same goes for False and 0
set21 = {"apple", 1,  "banana", 0, "cherry"}
set22 = {False, "google", 1, "apple", 2, True}

set23 = set21.intersection(set22)
print(set23)

# Difference
# difference() method will return a new set that will contain only the items from the first set that are not present in the other set
set24 = {"apple", "banana", "cherry"}
set25 = {"kiwi", "mango", "banana", "cherry"}
f = set24.difference(set25)
print(f)

# You can use the - operator instead of the difference() method, and you will get the same result.
set26 = {"apple", "banana", "mango"}
set27 = {"kiwi", "apple", "cherry", "grapes"}
g = set26 - set27
print(g)

# difference_update() method will also keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.
set28 = {"apple", "banana", "cherry"}
set29 = {"google", "microsoft", "apple"}
set28.difference_update(set29)
print(set28)

# symmetric_difference() method will keep only the elements that are NOT present in both sets
set30 = {"apple", "banana", "cherry"}
set31 = {"google", "microsoft", "apple"}
h = set30.symmetric_difference(set31)
print(h)

# You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.
i = set30 ^ set31
print(i)

# symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.
set32 = {"apple", "banana", "cherry"}
set33 = {"google", "microsoft", "apple"}
set32.symmetric_difference_update(set33)
print(set32)