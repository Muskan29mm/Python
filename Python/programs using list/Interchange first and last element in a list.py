# interchange first and last element of a list

def inter(a):
    a[0], a[-1] = a[-1], a[0]
    return a

a = [10,20,30,40,50,60,70,80,90,100]

print(inter(a))
