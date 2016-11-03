# create a function that returns it's input factorial

#import math
#print(math.factorial(8))

def factor(input):
    fact = 1
    for i in range(1,input+1):
        fact *= i
    return fact

print(factor(4))

def factor(input):
    fact = 1
    while input > 0:
        fact *= input
        input -= 1
    return fact

print(factor(4))
