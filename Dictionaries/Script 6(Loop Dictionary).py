# Loop through a dictionary

fruits = {
    "name" : "Apple",
    "quantity": "1kg",
    "price": "Rs.60"
}
# It will print only keys of dictionary
for x in fruits:
    print(x)

# To print values of dictionary
for x in fruits:
    print(fruits[x])

# You can also use "values()" method to return values of dictionary
for x in fruits.values():
    print(x)

# You can also use "keys()" method to return the keys of a dictionary
for x in fruits.keys():
    print(x)

# Loop through both keys and values, by using the items() method
for y in fruits.items():
    print(y)