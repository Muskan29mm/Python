# Python program to find Closest Pair to Kth index element in Tuple

test_list = [(3, 4), (78, 76), (2, 3), (9, 8), (19, 23)]

tup = (17, 23)

k = 1

res = min(test_list, key=lambda x: abs(x[k-1] - tup[k-1]))

print("The Nearest tuple to kth index element is :" + str(res))




# Given tup is (17, 23) and k is 1, the calculations are:
#
# For (3, 4): abs(3 - 17) which equals 14
# For (78, 76): abs(78 - 17) which equals 61
# For (2, 3): abs(2 - 17) which equals 15
# For (9, 8): abs(9 - 17) which equals 8
# For (19, 23): abs(19 - 17) which equals 2
# Therefore, output is (19, 23) because it has minimum difference
