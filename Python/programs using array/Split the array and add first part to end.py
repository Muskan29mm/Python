# Program for splitting the array and adding first part to end

arr = [10,20,30,40,50,60,70,80,90,100]
a = arr[:5]
print(a)

b = arr[5:]
print(b)

new_arr = b + a
print(new_arr)