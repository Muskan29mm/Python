# Looping in list

# Loop through a list
thislist = ["Apple", "Banana", "Cherry"]
for i in thislist:
    print(i)

# Loop through the index number
thislist = ["Apple", "Banana", "Mango", "Cherry"]
for i in range(len(thislist)):
    print(thislist[i])

# using while loop
fruits = ["Apple", "Banana", "Cherry", "Mango"]
i = 0
while i < len(fruits):
    print(fruits[i])
    i = i + 1

# Looping using list comprehension
thislist1 = ["Pineapple", "Guava", "Plum", "Orange"]
[print(x) for x in thislist1]
