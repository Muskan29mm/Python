# Program to find the sum of tuple

test_tup = (5, 20, 3, 7, 6, 8)
print(test_tup)

t1 = list(test_tup)
print(t1)

count = 0

for i in test_tup:
    count = count + i
print("Total count is", count)


