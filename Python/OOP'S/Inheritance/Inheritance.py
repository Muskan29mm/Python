# Inheritance

# Create a Parent class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


x = Person("John", "Roy")
x.printname()

print()

# Create a Child class
class Person1:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

# child class
class Student(Person1):
    pass

x1 = Student("Mike", "Olsen")
x1.printname()

print()


# This code doesn't inherit from parent class. Child class has it's own properties
class Person3:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student2(Person3):
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

x3 = Student2("Tanu", "Gaur")
x3.printname()

print()

# Add init() function to child class(inheriting from parent class) , Add a call to parent __init__ function
class Person2:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

# child class
class Student1(Person2):
    def __init__(self, fname, lname):
        Person2.__init__(self, fname, lname)

x2 = Student1("John", "Roy")
x2.printname()

print()

# using super() function.
# super() function will automatically inherit the methods and attributes of parent class. we don't have to use the name of parent class

class Person4:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student3(Person4):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

x4 = Person4("John", "Olsen")
x4.printname()

print()

# Add graduation year attribute to student class(Add Properties)
class Person5:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student4(Person5):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduation_year = 2014

x5 = Student4("Joe", "Mike")
print(x5.graduation_year)

print()

# Add Methods
class Person6:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student5(Person6):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduation_year = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to class of ", self.graduation_year)

x6 = Student5("John", "Jacobs", 2014)
x6.welcome()