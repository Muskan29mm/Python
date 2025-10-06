# Program to count occurrences of an element in a list(Say 50)

list1 = [10,50,2,90,50,10,5,3,8,90,50,6,1,50]
count = 0
for i in list1:
    if i == 50:
        count = count + 1
print(count)
