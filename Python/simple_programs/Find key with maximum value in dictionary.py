# Find key with maximum value in dictionary

dict1 = {"apple": 3, "banana": 12, "orange": 6, "mango": 8}
a = sorted(dict1.values())
print("Sorted values:", a)

for key in dict1:
    if dict1[key] == a[-1]:
        print("Key with maximum value:", key)