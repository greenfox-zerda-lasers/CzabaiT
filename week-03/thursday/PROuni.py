
def union(list1,list2):
    new_list = list1
    for i in range(0,len(list1)):
        if list2[i] not in list1:
            new_list.append(list2[i])
    new_list.sort()
    return new_list

print(union([4,5,6],[1,2,3]))
print(union([4,5,7],[4,1,7]))