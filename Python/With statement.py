# # With statement in python
#
# # Open the file using 'with' statement
# with open('example', 'r') as file:
#     content = file.read()
#     print(content)
#
# # Writing to a file
# with open("example", 'w') as file:
#     file.write("Hello! This is Python with statement example")
#
# # Context Mangers and "with" statement
# class FileManager:
#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode
#
#     def __enter__(self):
#         self.file = open(self.filename, self.mode)
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.file.close()
#
# with FileManager('example', 'w') as f:
#     f.write("Using context Manager!")

# Function based context managers
from contextlib import contextmanager

@contextmanager
def open_file(filename, mode):
    file = open(filename, mode)
    try:
        yield file
    finally:
        file.close()

with open_file("example", 'w') as f:
    file = f.write("Writing using functions based context managers ")