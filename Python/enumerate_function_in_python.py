# Enumerate function in python

# Enumerate() function adds a counter to any iterable. It turns the variable into something we can loop through where each item comes with it's number

a = ["Hello", "How", "are", "You"]

for i, name in enumerate(a):
    print(f"Index {i}: {name}")

print(list(enumerate(a)))

