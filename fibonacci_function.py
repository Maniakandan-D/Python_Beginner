def fibonacci(n: int) -> int:  # annotations for hint
    """Return the 'n' th Fibonacci number , for positive 'n'...# doc string ctrl+Q"""
    if 0 <= n <= 1:
        return n
    n_minus1, n_minus2 = 1, 0
    result = None  # Fibonacci series only positive values
    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result


for i in range(21):  # first 20 fibonacci numbers print
    print(i, fibonacci(i))
