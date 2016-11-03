import math

def initial_sorting(list):
    if list == sorted(list):
        print("Initially sorted")
    else:
        print("Initially UNsorted")
        list.sort()
    return list



def binary_search(list,target):
    initial_sorting(list)

    lower = 0
    upper = len(list)-1

    middle = 0
    found = -1

    while found != middle:
        if lower > upper:
            found = "Target isn't in the list!"
            break
        else:
            middle = math.floor( (lower+upper) /2 )
            mid_value = list[middle]
            if mid_value < target:
                lower = middle + 1
            elif mid_value > target:
                upper = middle - 1
            else:
                found = middle

    return found

print(binary_search([4,5,6], 4))
print(binary_search([4,5,7], 6))

