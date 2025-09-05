print("\nRight-sided Pyramid")
rows = 8
for i in range(1, rows + 1):
    x = '* ' * i  # Create a string with i stars
    print(f'{x: >{2*rows}}')  # Right-align the text within 2*rows width
