list = [10,20,30,40,50,60,70,80,90,100]
mult = 1
for i in list:
    mult = mult * i
print(mult)


# using function
def mult(list1):
    mult = 1
    for i in list1:
        mult = mult * i
    return mult
list1 = [10,20,30]

print(mult(list1))