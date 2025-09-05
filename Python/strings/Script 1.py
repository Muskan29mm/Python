# To display a string
print("Hello")

# Quotes inside Quotes
print("He is 'Johnny'")
print('He is "Johnny"')

# Multiline String
a = """This is all about string. This is a text
for giving example of multiline string. Multiline string
can be written inside three quotes.
"""
print(a)

# Accessing the elements of the string
b = "Hello World!"
print(b[3])


# Looping through a string
for x in b:
    print("\n", x)

# Check string
print("example" in a)

# Check using if statement
if "about" in a:
    print('about' in a)

# Check if not
c = "The best things in life are free!"
if "expensive" not in c:
    print("No, 'expensive' is  not present")

# Slicing
print(b[3:])
print(b[:3])

# Checking at specific position
print(b[2:7])

# slice from start
print(b[:5])

# slice from end
print(b[3:])

# Negative indexing
print(b[-5:-2])

# Upper method (Convert string to upper)
print(b.upper())

d = "HELLO"
# Lower method (Convert string to lower)
print(d.lower())

# Remove whitespace
e = " Hello World "
print(e.strip())

# Replace string
print(b.replace('H', 'J'))

# Split string
e = "Hello, World!"
print(e.split(','))

# Concatenate a string
f = "Hello"
g = "World"
h = f + g
print(h)

# Concatenate a string while adding a space
i = f + " " + g
print(i)

# Using f-string
age = 36
txt = f"My name is john and my age is {age}"
print(txt)

name = "john"
txt1 = f"My name is {name} and my age is 36"
print(txt1)

# Perform math operation using f-string
txt2 = f"The price is {20 * 59} dollars"
print(txt2)

price = 59
txt3 = f"The price is {price:.2f} dollars"
print(txt3)

# Escape character
# Adding a character in string is illegal, so to add a string we use backslash (\)
txt4 = "We are the so-called \"Vikings\" from the north."
print(txt4)
