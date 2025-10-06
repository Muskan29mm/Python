def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def print_prime_numbers(start, end):
    for i in range(start, end + 1):
        if is_prime(i):
            print(i)


start = int(input("Enter the starting range:"))
end = int(input("Enter the ending range: "))

print("The prime numbers between {start} and {end} are :")
print_prime_numbers(start, end)
