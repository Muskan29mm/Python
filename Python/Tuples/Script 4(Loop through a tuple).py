# Loop through a tuple

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

# Loop through the index numbers
for i in range(len(thistuple)):
    print(thistuple[i])

# loop through tuple using while loop
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1
