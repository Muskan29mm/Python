# "disjoint" describes two sets (or other iterables) that have no common elements
# Program to check if two sets are disjoint

set1 = {1,2,3,4,5}
set2 = {9,8,7,6,12}

if set1.isdisjoint(set2):
    print("Sets are disjoint")
else:
    print("Sets are not disjoint")