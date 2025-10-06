# Iterators in python

mytuple = ("Banana", "Apple", "Cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))


print()

# Strings are also iterable objects and can return an iterable
mystr = "Banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

print()

# Looping through an iterable object
mytuple = ("Apple", "Banana", "Cherry")
for x in mytuple:
    print(x)

print()

# Iterate the characters of a string
mystr = "Apple"
for x in mystr:
    print(x)


print()

# Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.)
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
