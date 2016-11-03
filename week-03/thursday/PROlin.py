list1 = [4,5,6]
list2 = [4,5,7]

def linear_search(list,search):
    res = -1
    for i in range(0,len(list)):
        if search == list[i]:
            res = i
    return res

print(linear_search(list1,6))
print(linear_search(list2,6))
