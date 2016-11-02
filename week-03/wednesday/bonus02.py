# 6 count number of even and odd numbers for a series of number

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

i = 0
even = 0
odd = 0
zero = 0

while i < len(numbers):
    if numbers[i] % 2 == 0:
        even += 1
    elif numbers[i] % 2 == 1:
        odd += 1
    else:
        zero += 1
    i += 1

print('even:', even, ' odd:', odd, ' zero:', zero)