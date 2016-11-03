numbers = [4, 5, 6, 7, 8, 9, 10]
# write your own sum function

def summarize(input):
    summ = 0
    for i in input:
        summ += i
    return summ

print(summarize(numbers))