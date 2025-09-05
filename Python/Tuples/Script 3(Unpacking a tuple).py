# packing and unpacking a tuple
fruits = ("apple", "banana", "cherry")  # packing a tuple
print(fruits)

# unpacking means extract the values back into variables
(green, yellow, red) = fruits # unpacking a tuple
print(green)
print(yellow)
print(red)

# using asterisk(*)
# if the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list
fruits1 = ("apple", "banana", "cherry", "mango", "strawberry", "pineapple")
print(fruits1)
(green, yellow, *red) = fruits1

print(green)
print(yellow)
print(red)

# if the asterisk(*) is added to another variable name than the last, python will assign values until the number of values left is equal to the number of variables left
(green, *yellow, red) = fruits1
print(green)
print(yellow)
print(red)