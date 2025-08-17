# File Handling

# opening a file
f = open("/home/muskan/PycharmProjects/Python/Python/File Handling/demo_file", "r")
print(f.read())

print()
print("____________________________________________________")

# You can also use 'with' statement
with open("/home/muskan/PycharmProjects/Python/Python/File Handling/demo_file", 'r') as e:
    print(e.read())

print()
print("____________________________________________________")

# While use with statement you do not need to close the file, but when not opening file using "with" statement you need to close the file
# "With" statement automatically closes the files

# CLOSING THE FILE AS HERE IN THIS EXAMPLE WE ARE NOT USING "WITH" STATEMENT
f1 = open("/home/muskan/PycharmProjects/Python/Python/File Handling/demo_file", "r")
print(f1.readline())
f1.close()

print()
print("____________________________________________________")

