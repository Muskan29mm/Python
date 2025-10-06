tuple_list = [(15, 3), (3, 9)]

lst = []

for i in tuple_list:
    for num in i:
        lst.extend(list(str(num)))


lst = lst[::-1]

seen = set()
unique_digits = []

for digit in lst:
    if digit not in seen:
        seen.add(digit)
        unique_digits.append(int(digit))

print("Output result:", unique_digits)