list1 = [1,2,3,4,0,89,56,79,45]
print("The list before clearing is: ",list1)
list1.clear()
print("The list after clearing is: ",list1)

# using pop method
list1 = [1,2,3,4,5,6,7,8,9,20]
print("The list before deleting is: ",list1)
while (len(list1) != 0):
    list1.pop()
print("The list after deleting is: ",list1)