# Program to find duplicate from list

list = [1, 2, 3, 4, 5, 1, 2, 3, 6, 7, 8, 9, 10]
a = []

for i in list:
    if i not in a:
        a.append(i)

print("List after removing duplicates:", a)