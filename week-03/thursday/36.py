import copy

numbers = [3, 4, 5, 6, 7]
# write a function that reverses a list

def rev(input):
    rev_numbers = []
    n = len(input)
    for i in range(0,n):
         rev_numbers.append(input[n-1-i])
    return rev_numbers

print(rev(numbers))

def rev2(list):
    rev_list = []
    for i in reversed(list):
        rev_list.append(i)
    return rev_list

print(rev2(numbers))

def rev3(list):
    x = copy.copy(list)
    x.reverse()
    return x

print(rev3(numbers))


