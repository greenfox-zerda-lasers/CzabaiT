def order(sentence):
    dict = {}
    string =''

    words = sentence.split()
    for word in words:
        for letter in word:
            try:
                number = int(letter)
                dict[number] = word
                print(dict)
            except ValueError:
                continue


    for i in dict:
        string += dict[i] + ' '

    return string[:-1]

#order("is2 Thi1s T4est 3a")
print(order("is2 Thi1s T4est 3a"))
