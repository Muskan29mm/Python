def sum(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum


a = input("Enter the elements in array : ")

a = list(map(int, a.split()))


ans = sum(a)


print("The sum of elements of an array is", ans)
