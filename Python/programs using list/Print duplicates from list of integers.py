# Program to print duplicates from a list of integers

a = [1, 2, 3, 1, 2, 4, 5, 6, 5]
li = []
duplicates = set()

for i in a:
    if i in li:
        duplicates.add(i)
    else:
        li.append(i)

for item in duplicates:
    print(item)



