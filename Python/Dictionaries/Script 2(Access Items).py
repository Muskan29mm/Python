# Access items in dictionary

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
a = thisdict["year"]
print(a)

# Another method is get() which will give same result
b = thisdict.get("model")
print(b)

# To return all the keys in dictionary use 'keys()' method
c = thisdict.keys()
print(c)

# Add a new item to the original dictionary, and see that the keys list gets updated as well:
thisdict["color"] = "white"
print(c)

# get values of the dictionary
d = thisdict.values()
print(d)

# Make a change in the original dictionary, and see that the values list gets updated as well
thisdict["year"] = 2000
print(thisdict)

# Get Items
e = thisdict.items()
print(e)

# The returned list is a view of the items of the dictionary, meaning that any changes done to the dictionary will be reflected in the items list.
thisdict["year"] = 1990
print(e)

# Check if the keys exists
if "brand" in thisdict:
    print("Yes, 'brand' key is present in thisdict dictionary")