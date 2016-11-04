# create a function that takes a list and returns a new list with all the elements doubled
list = [5,6,7,8,9]
new_list = []

def doubler(list):
    new_list = []
    for i in list:
        new_list.append(2*i)
    return new_list

print(doubler(list))