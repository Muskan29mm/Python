# Python program to remove a key from dictionary

dict1 = {
    'Hema': 21,
    'Yash': 24,
    'Neha': 20,
    'Sonal': 23,
    'Isha': 25
}
print("The dictionary before removing is:", str(dict1))

a = dict1.pop('Hema')
print("The removed Key value is", str(a))

print("The dictionary after remove is:", str(dict1))
