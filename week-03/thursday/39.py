names = ['Zakarias', 'Hans', 'Otto', 'Ole']
# create a function that returns the shortest string
# from a list

def shortest(list):
    shortest = list[0]
    for i in list:
        if len(i) < len(shortest):
            shortest = i
    return shortest

print(shortest(names))