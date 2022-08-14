def fib(n):
    if n<2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

n = int(input("type your value: "))

print(f'The {n}th number is: {fib(n)}')