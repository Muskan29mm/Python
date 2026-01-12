# Program to find largest of three numbers

def largest_of_three(x,y,z):
    if (x >= y) and (x >= z):
        return x
    elif (z >= y) and (z >= x):
        return z
    else:
        return y
    
print(largest_of_three(10, 80, 30))
