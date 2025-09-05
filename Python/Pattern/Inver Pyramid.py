print("\nInvert Pyramid")
rows = 10
for i in range(rows, 0, -1):
    x = '* ' * i
    print(f'{x:^{2*rows}}')  # Center-align the text within 2*rows width
