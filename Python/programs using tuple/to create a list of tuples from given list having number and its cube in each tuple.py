# Python Program to create a list of tuples from a given list having number and it's cube

list_1 = [1,2,3,4,5]


res = [pow(i,3) for i in list_1]
print(res)