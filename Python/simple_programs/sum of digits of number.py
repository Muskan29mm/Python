# Program to find sum of digit of number

def sum_of_digits(number):
    total = 0

    for digit in str(number):
        total = total + int(digit)
    return total
    
input_num = 12345
digit_sum = sum_of_digits(input_num)
print("Sum of digits:", digit_sum)