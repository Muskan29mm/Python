# Python program ot find maximum and minimum of K elements in tuple

test_tup = (5, 20, 3, 7, 6, 8)

print("The original tuple is : " + str(test_tup))

K = 1

res = []


sorted_tup = sorted(test_tup)
print("The sorted tuple is : " + str(sorted_tup))

res.extend(sorted_tup[:K])  # First K elements
res.extend(sorted_tup[-K:]) # Last K elements

res = tuple(res)

print("The extracted values : " + str(res))