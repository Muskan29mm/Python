# lambda function can take any number of arguments but can have only one expression

x = lambda a : a + 10
print(x(5))

# multiple arguments but one expression
x = lambda a, b : a + b
print(x(3,4))

x = lambda a, b, c : a * b * c
print(x(2,2,2))

def myfunc(n):
  return lambda a : a + n

mydoubler = myfunc(3)

print(mydoubler(11))