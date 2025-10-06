# Here N is like how many largest number to find, like if value of N is 3 then it will give output of first 3 largest number i.e
# which are the 3 most largest number in the list

list1 = [2, 6, 41, 0, 3, 50, 6, 10]
final_list = []
N = 3
for i in range(0, N):
    max_value = 0
    max_index = -1
    for j in range(len(list1)):
        if list1[j] > max_value:
            max_value = list1[j]
            max_index = j

    if max_index != -1:
        list1.pop(max_index)
        final_list.append(max_value)

print(final_list)
