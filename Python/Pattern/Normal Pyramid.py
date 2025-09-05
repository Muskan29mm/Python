print("\nNormal Pyramid")
rows = 10
for i in range(1, rows + 1):
    x = '* ' * i  # Create a string with i stars
    print(f'{x:^{2*rows}}')  # Center-align the string within 2*rows width
