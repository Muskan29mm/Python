# Dictionary

thisdict = {
    "model": "mustang",
    "brand": "Ford",
    "year": 1964
}
print(thisdict)

# print the "brand" value of dictionary
print(thisdict["brand"])

# Duplicates not allowed, it overwrite the value
dict1 = {
    "model": "mustang",
    "brand": "Ford",
    "year": 1964,
    "year": 1978
}
print(dict1)

# To determine how many items a dictionary have use "len()" function
print(len(dict1))

# Dictionary Items - Data Types
thisdict1 = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict1)

# To determine type
print(type(thisdict1))

# Construct dictionary using dict() constructor
dict2 = dict(brand = "Ford", model = "mustang", year = 1966)
print(dict2)
