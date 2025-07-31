# Nested dictionary

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)

# You can add three dictionaries into a new dictionary
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

family = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}
print(family)

# Access Items in Nested Dictionaries. ex:- print the name of child2
print(family["child2"]["name"])

# loop through nested dictionary
for x in myfamily.items():
    print(x)
