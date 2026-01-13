# # Program to reverse a number

# def reverse_number(number):
#     reversed_num = 0

#     while number > 0:
#         digit = number % 10
#         reversed_num = (reversed_num * 10) + digit
#         number = number // 10
#     return reversed_num

# input_num = 12345
# reversed_num = reverse_number(input_num)
# print("Reversed Number:", reversed_num)

number = str(19029)
print(str(number)[::-1])
