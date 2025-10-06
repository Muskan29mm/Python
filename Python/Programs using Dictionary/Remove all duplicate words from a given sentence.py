# Program to remove all duplicate words from a given sentence

s1 = "Geeks for Geeks"
s2 = s1.split()
print(s2)

a = list(set(s2))
print(a)

b = " ".join(a)
print(b)
