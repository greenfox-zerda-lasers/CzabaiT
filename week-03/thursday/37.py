numbers = [3, 4, 5, 6, 7]
# write a function that filters the odd numbers
# from a list and returns a new list consisting
# only the evens

def odd_filter(list):
    new_list = []
    for i in list:
        if i % 2 == 0:
            new_list.append(i)
    return new_list

print(odd_filter(numbers))