def rotate_array_one_by_one(arr, d):
    n = len(arr)
    # Handling cases where d >= n
    d = d % n

    for i in range(d):
        # Store the first element
        temp = arr[0]
        # Shift all elements one position to the left
        for j in range(n - 1):
            arr[j] = arr[j + 1]
        # Place the first element to the end of the array
        arr[n - 1] = temp
    return arr


# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7]
d = 3
rotated_arr = rotate_array_one_by_one(arr, d)
print("Rotated Array by rotating one by one:", rotated_arr)

