# While loop

count = 0
while (count < 3):
    count = count + 1
    print("Hello world")

# Infinite loop
# age = 28
#
# while (age > 20):
#     print('Infinite loop')

# While loop with continue statement (# Prints all letters except 'e' and 'l')
i = 0
a = "Hello world"

while i < len(a):
    if a[i] == 'e' or a[i] == 'l':
        i += 1
        continue
    print(a[i])
    i += 1

# While loop with break statement (Break Statement brings control out of the loop.)
i = 0
b = "Hello World"

while i < len(b):
    if b[i] == "o" or b[i] == "l":
        i += 1
        break
    print(b[i])
    i += 1

# While loop with pass statement (to write empty loops)
a = "Hello world"
i = 0

while i < len(a):
    i += 1
    pass

print("Value of i: ", i)

# while-else loop
i = 0
while i < 4:
    i += 1
    print(i)
else:
    print("No Break 1")

i = 0
while i < 4:
    i += 1
    print(i)
    break
else:
    print("No Break")