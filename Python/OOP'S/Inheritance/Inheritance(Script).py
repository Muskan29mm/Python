# Inheritance(Types of inheritance)

# Single Inheritance
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

emp = Employee("John", 23000)
print("----------------SINGLE INHERITANCE----------------")
print(emp.name, emp.salary)

print()

# Multiple Inheritance
class Person:
    def __init__(self, name):
        self.name = name

class Employee:
    def  __init__(self, salary):
        self.salary  = salary

class Job(Person, Employee):
    def __init__(self, name, salary):
        Person.__init__(self, name)
        Employee.__init__(self,salary)

    def print(self):
        print(self.name, self.salary)

s1 = Job("Joe", 24000)
print("------------------------MULTIPLE INHERITANCE--------------")
print(s1.name, s1.salary)

print()

# Multilevel Inheritance
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

class Job(Employee):
    def __init__(self, name, salary, role):
        super().__init__(name, salary)
        self.role = role

    def print(self):
        print(self.name, self.salary, self.role)

s2 = Job("Jack", 25000, "Manager")
print("-------------------MULTILEVEL INHERITANCE-----------------")
print(s2.name, s2.salary, s2.role)

print()

# Hierarchical Inheritance
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

class Job(Person):
    def __init__(self, name, salary, job):
        super().__init__(name)
        self.salary = salary
        self.job = job

    def print(self):
        print(self.name, self.salary, self.job)

s3 = Job("Roy", 5500, "Tester")
print("----------------------HIERARCHICAL INHERITANCE--------------------")
print(s3.name, s3.salary, s3.job)

print()

# Hybrid Inheritance
class Person:
    def __init__(self, name):
        self.name = name

# Derived class from Person (Multilevel)
class Employee1(Person):
    def __init__(self, name, emp_id):
        super().__init__(name)
        self.emp_id = emp_id

# Another base class
class Department:
    def __init__(self, dept):
        self.dept = dept

# Derived class from Employee and Department (Hybrid = Multilevel + Multiple)
class Manager(Employee1, Department):
    def __init__(self, name, emp_id, dept, level):
        Employee1.__init__(self, name, emp_id)
        Department.__init__(self, dept)
        self.level = level

    def display(self):
        print(f"Name: {self.name}, ID: {self.emp_id}, Dept: {self.dept}, Level: {self.level}")

# Create object
m1 = Manager("Alice", 101, "HR", "Senior")

print("---------------HYBRID INHERITANCE---------------")
m1.display()
