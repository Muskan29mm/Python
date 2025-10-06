# Python program to find sum of all values in a dictionary

dict = {
    'a':100,
    'b':200,
    'c':300
}

sum = 0

for i in dict.values():
    sum+= i
print(sum)