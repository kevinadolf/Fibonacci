def fib(n, memo):
    if n<2:
        return 1
    else:
        memo [n] = fib(n-1, memo) + fib(n-2, memo)
        return memo[n]


memo = [1]*100

n = int(input("type your value: "))

print(f'The {n}th number is: {fib(n, memo)}')