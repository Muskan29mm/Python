def largest(arr, n):
    max_val = arr[0]

    for i in range(1,n):
        if arr[i] > max_val:
            max_val = arr[i]

    return max_val

a = input("Enter the elements in an array: ")

# Splitting the string into individual elements and converting them to integers
arr = list(map(int, a.split()))

l = len(arr)

ans = largest(arr, l)

print("The largest element in the array is:", ans)



