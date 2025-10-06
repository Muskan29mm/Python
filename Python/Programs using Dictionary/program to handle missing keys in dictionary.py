# Python program to handle missing keys in dictionary

# Using key
dict = {'a':4, 'b':7, 'c':1}
if 'd' in dict:
    print(dict["d"], "Key is present in dictionary")
else:
    print("Key is not Present in dictionary")


# using get
country_code = {'India': '0091',
                'Australia': '0023',
                'Canada': '1548'}

print(country_code.get('India'))

print(country_code.get('Malaysia'))

# using set default
country_code = {'India': '0091',
                'Australia': '0025',
                'Nepal': '00977'}

# Set a default value for Japan
country_code.setdefault('Japan', 'Not Present')

print(country_code['India'])
print(country_code['Japan'])
