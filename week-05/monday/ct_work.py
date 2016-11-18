from collections import Counter

def anagramm(string1, string2):
    return sorted(string1.replace(' ','').lower()) == sorted(string2.replace(' ','').lower())

def count_letter(string):
    return Counter([i.lower() for i in string if i.isalpha()])

