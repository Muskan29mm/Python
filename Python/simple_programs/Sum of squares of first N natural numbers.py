# Program to print the sum of squares of first N natural numbers
a = int(input("Enter the value of N (N as natural numbers):"))

sum_of_squares = 0

for i in range(1, a + 1):
    sum_of_squares += i * i

print("Sum of squares of the first", a, "natural numbers is:", sum_of_squares)