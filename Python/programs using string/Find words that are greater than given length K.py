# Python program to find those words that are greater than k

words = ["Strings", "cat", "Mat", "Yatch", "Fold", "Water"]

k = 3

for i in words:
    if len(i)>k:
        print("The Words are: ", i)
