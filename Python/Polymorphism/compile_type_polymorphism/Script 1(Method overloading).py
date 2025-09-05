# Compile type polymorphism(Method overloading)
# Multiple methods with same name but with different parameters

class MathOperations:
    def add(self, *args):
        return sum(args)


obj = MathOperations()
print(obj.add(5, 5))
print(obj.add(5, 5, 5))




