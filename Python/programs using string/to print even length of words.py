# Python program to print even length of words from a string

string = "Peacock is National Bird of India"

s = string.split(" ")
print(s)
for i in s:
    if len(i)%2==0:
        print(i)
