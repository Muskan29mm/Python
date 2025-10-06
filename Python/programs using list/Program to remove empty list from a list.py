# Python program to remove empty list from a list

l1 = [10, 20, 3, [], 50, 70, 30, 90, 100]
new_list = [i for i in l1 if i !=[]]
print(new_list)



