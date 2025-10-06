# Print all prime numbers in a range

x, y = 2, 30
lst = []
def print_prime():
   for i in range(x, y+1):
        if i <= 1:
            continue
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                break
        else:
            lst.append(i)

   print(lst if lst else "No")

print_prime()