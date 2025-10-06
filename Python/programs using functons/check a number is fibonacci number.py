import math

def is_perfect_square(x):
    s = int(math.sqrt(x))
    return s * s == x

def is_fibonacci(n):
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

a = int(input("Enter a number:"))


if is_fibonacci(a):
    print(a, "is a fibonacci number")
else:
    print(a, "is not a fibonacci number")
