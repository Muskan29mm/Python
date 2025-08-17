# Read a File


# By default, read method returns the whole text but you can specify how many characters you want to return
with open("/home/muskan/PycharmProjects/Python/Python/File Handling/demo_file", "r") as f:
    print(f.read(5))

print()
print("____________________________________________________")

# ReadLine()
# User can return one line by using readline() method
with open("/home/muskan/PycharmProjects/Python/Python/File Handling/demo_file", "r") as f:
    print(f.readline())

print()

print("____________________________________________________")

# By calling readline() two times, you can read the two first lines
with open("/home/muskan/PycharmProjects/Python/Python/File Handling/demo_file", "r") as f:
    print(f.readline())
    print(f.readline())

print()

print("____________________________________________________")

# By looping through the lines of the file, you can read the whole file, line by line
with open("/home/muskan/PycharmProjects/Python/Python/File Handling/demo_file") as f:
  for x in f:
    print(x)
print("____________________________________________________")