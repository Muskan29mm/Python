# Remove Items from dictionary

# using "pop" method. It will remove specified item from dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
thisdict.pop("model")
print(thisdict)

# using "popitem" method. It will remove last item from dictionary
thisdict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict1)
thisdict1.popitem()
print(thisdict1)

# del keyword remove the specified item with the key name
car = {
"brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car)
del car["model"]
print(car)

# del can also be used to delete whole dictionary
car1 = {
"brand": "Ford",
  "model": "Mustang",
  "year": 2000
}
print(car1)
# del car1
# print(car1)

# The "clear" method empties the dictionary
car2 = {
"brand": "Ford",
  "model": "Mustang",
  "year": 2002
}
print(car2)
car2.clear()
print(car2)