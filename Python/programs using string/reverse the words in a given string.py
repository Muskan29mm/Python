# python program to reverse the words in a given string

string = "Hello! How are You"

rev = string.split()[::-1]
print(rev)

l=[]
for i in rev:
    l.append(i)
print(" ".join(l))