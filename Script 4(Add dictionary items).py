# Add items in dictionary

thisdict = {
    "brand": "Ford",
    "model": "mustang",
    "year":  1965
}
print(thisdict)
thisdict["color"] = "red"
print(thisdict)

# using update()  method. Add a color item to the dictionary by using the update() method
thisdict1 = {
    "brand": "Ford",
    "model": "mustang",
    "year":  1965
}
print(thisdict1)
x = thisdict1.update({"color": "red"})
print(thisdict1)

