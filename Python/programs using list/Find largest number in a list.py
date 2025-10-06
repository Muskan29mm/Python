list1 = [10,12,30,50,607,100,1002,33,506]
largest = list1[0]

for i in list1:
    if i > largest:
        largest = i
print("The largest element in a list is", largest)
print("The value of i is", i)

# using function
def largest(list1):
    largest = list1[0]

    for i in list1:
        if i > largest:
            largest = i
    return largest

list1 = [10,12,30,50,607,100,1002,33,506]

print("The largest element in a list is", largest(list1))
print("The value of i is", i)



