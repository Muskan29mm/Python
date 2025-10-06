# Program too remove all duplicates from a given string in python

string = "National Bird is peacock and National animal is Bengal Tiger"
t = ""
for i in string:
    if i in t:
        pass
    else:
        t = t + i
print(t)