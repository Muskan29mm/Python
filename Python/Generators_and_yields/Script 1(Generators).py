# Generators in python

# Example for generator function
def func(max):
    cnt = 1
    while cnt <= max:
        yield cnt
        cnt += 1

ctr = func(5)
for n in ctr:
    print(n)

print()

# Creating generators
def fun():
    yield 1
    yield 2
    yield 3

for val in fun():
    print(val)

print()

# Using "return" instead of "yield"
def fun1():
    return 1 + 2 + 3

res = fun1()
print(res)