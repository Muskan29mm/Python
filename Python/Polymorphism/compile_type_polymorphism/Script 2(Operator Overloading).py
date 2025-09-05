# Compile type polymorphism(Operator overloading)
# Redefining the definition of predefined operator (User defined operator)

class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages


b1 = Book(100)
b2 = Book(150)

print(b1 + b2)


# Description of above code
# b1 = Book(100) and b2 = Book(150) create two Book objects. b1 has 100 pages, and b2 has 150 pages.
#
# The expression b1 + b2 calls the __add__ method of the Book class.
#
# Inside the __add__ method, self refers to b1 (with self.pages being 100), and other refers to b2 (with other.pages being 150).
#
# The method returns the sum of self.pages and other.pages, which is 100 + 150 = 250.
#
# The print() function then displays this result.