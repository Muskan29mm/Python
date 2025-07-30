# Copying a dictionary

# using a copy() method
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
a = thisdict.copy()
print(a)

# use built-in method called "dict"
fruits = {
    "name" : "Apple",
    "quantity": "1kg",
    "price": "Rs.60"
}
b = dict(fruits)
print(b)