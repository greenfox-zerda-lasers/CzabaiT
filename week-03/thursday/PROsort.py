
def bubble_sort(list):
    width = len(list)
    for i in range(0,width):
        for j in range(0,len(list)-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
        width -= 1
    return list


print(bubble_sort([3,9,4,5,2,1]))