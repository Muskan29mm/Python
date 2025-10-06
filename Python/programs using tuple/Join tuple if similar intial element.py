# Python join tuple if similar initial element

from collections import defaultdict

test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)]

# Dictionary to group by first element
grouped = defaultdict(list)

for tup in test_list:
    grouped[tup[0]].append(tup[1])


res = [(key, *vals) for key, vals in grouped.items()]

print(res)