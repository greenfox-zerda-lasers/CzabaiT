# 1. write a recursive function
# that takes one parameter: n
# and counts down from n

def recursive(n):
    if n < 1:
        print(n)
        return 0
    else:
        print(n)
        return recursive(n-1)


recursive(5)