# Program to find simple interest
def simple_interest(p, r, t):
    s1 = p*r*t/100
    return s1


p = int(input("Enter the principal: "))
r = int(input("Enter the rate: "))
t = int(input("Enter the time: "))

print("The Simple Interest is", simple_interest(p,r,t))
