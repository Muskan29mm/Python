# Program to find Compound Interest

def compound_Interest(p, r, t):
    amount = p * (pow((1 + r / 100), t))
    ci = amount - p
    return ci

p = int(input("Enter the amount of principal: "))
r = float(input("Enter the amount of Rate: "))
t = int(input("Enter the time: "))

print("The Compound Interest is", compound_Interest(p,r,t))
