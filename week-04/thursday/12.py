# 12. write a recursive function that can add numbers in
listácska = [1, 2, [3, 4], 1, [1, [2, 4]]]


def list_add(listácska):
    if len(listácska) == 0:
        return 0

    elif type(listácska[0]) == list:
        return list_add(listácska[0]) + list_add(listácska[1:])
    else:
        return listácska[0] + list_add(listácska[1:])


print(list_add(listácska))