# Create a method that returns the five most frequent lottery number in a pretty table format
import operator
from prettytable import PrettyTable

def five_most_frequent(file_name):
    list = []

    with open(file_name,'r') as fin:
        for line in fin:
            numbers = [int(s) for s in line.split(';')[-5:]]
            list.extend(numbers)

    freq = {x: list.count(x) for x in list}
    sorted_freq = sorted(freq.items(), key=operator.itemgetter(0))
#   print(sorted_freq)
    csv_format(sorted_freq)


def csv_format(sorted_freq):
    table = PrettyTable(["number", "frequency"])
    table.add_row(sorted_freq[0])
    table.add_row(sorted_freq[1])
    table.add_row([sorted_freq[2][0], sorted_freq[2][1]])
    table.add_row([sorted_freq[3][0], sorted_freq[3][1]])
    table.add_row([sorted_freq[4][0], sorted_freq[4][1]])
    table.sortby = "frequency"
    table.reversesort = True
    print(table)

five_most_frequent('otos.csv')