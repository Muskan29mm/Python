try:
    print(x)
except:
    print("Exception occurred")

# Many Exceptions
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

# Else
# use the else keyword to define a block of code to be executed if no errors were raised
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

# Finally
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try-except' is finished")

# raise an exception
x = -1
if x < 0:
    raise Exception("No number below 0 are allowed")
