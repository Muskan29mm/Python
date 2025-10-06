# Program to remove empty tuples from a list

list1 = [(1, 2), (), (3, 4), (), (5,)]
new_list = [i for i in list1 if i !=()]
print(new_list)