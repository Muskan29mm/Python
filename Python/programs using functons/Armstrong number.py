def armstrong(num):
    sum_of_powers = 0
    n1 = len(str(num))
    temp = num
    while temp > 0:
        digit = temp % 10
        sum_of_powers += digit ** n1
        temp //= 10
    return sum_of_powers

num = int(input("Enter the Number:"))

if num == armstrong(num):
    print("The", num, "is Armstrong Number")
else:
    print("The", num, "is Not an Armstrong Number")