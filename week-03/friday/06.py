# create a function that takes a list and returns a ((new)) list that is reversed
import math

list1 = [3,4,5,6,7]

#lista feléig iterál (páratlan elemszámú lista közepe fordítás után is középen van)
def swap(list):
    for i in range(0,math.floor(len(list)/2)):
        list[i], list[len(list)-1-i] = list[len(list)-1-i], list[i]
    return list

print(swap(list1))

