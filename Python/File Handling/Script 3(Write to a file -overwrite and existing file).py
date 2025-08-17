# File Write

# Open the demo_file and append more content
with open("/home/muskan/PycharmProjects/Python/Python/File Handling/demo_file", "a") as f:
    f.write("Now file has more content!\n")

with open("/home/muskan/PycharmProjects/Python/Python/File Handling/demo_file", "r") as f:
    print(f.read())

print()

# To overwrite the existing content to the file, use "W" parameter
with open("/home/muskan/PycharmProjects/Python/Python/File Handling/demo_file", "w") as f:
    f.write("Now the file content has changed")

with open("/home/muskan/PycharmProjects/Python/Python/File Handling/demo_file") as f:
    print(f.read())

print()

# To create a new file
f = open("myfile.txt", "x")
