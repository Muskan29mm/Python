# JSON is a format for storing and exchanging data

import json # JSON is a in-built package in python
# to pass a JSON string you can use json.loads() methods
# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

# python object can be converted to JSON strings by using json.dumps() methods
import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

# converting different python objects to JSON strings
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))  # list gets converted into array
print(json.dumps(("apple", "bananas")))  # tuple gets converted into array
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# to format the result json.dumps() has method called indent to define number of indents
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use four indents to make it easier to read the result:
print(json.dumps(x, indent=4))

