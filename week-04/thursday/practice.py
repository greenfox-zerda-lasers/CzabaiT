def fibonacci(n):
    print("fibonacci:" + str(n))
    if n<2:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

print(fibonacci(8))