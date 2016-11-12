# 4. Given base and n that are both 1 or more, compute recursively (no loops)
# the value of base to the n power, so powerN(3, 2) is 9 (3 squared).

def recursive(base, n):
    if n == 1:
        return base * n
    else:
        return base * recursive(base, n-1)

print(recursive(3,3))