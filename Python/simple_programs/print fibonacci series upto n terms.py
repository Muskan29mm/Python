# Print fibonnaci series upto n terms

def fibonacci_series(n):
    a, b = 0, 1
    series= []
    for i in range(n):
        series.append(a)
        a, b = b, a + b
    return series

n_terms = 10
fib_series = fibonacci_series(n_terms)
print(fib_series)