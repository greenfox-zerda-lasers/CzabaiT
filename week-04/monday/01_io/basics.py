# 1. Create a method that reads all contents of a file when its name given as param
def readfile(file_name):
    f = open(file_name)
    result = f.read()
    f.close()
    return result

#print(readfile('texts/zen_of_python.txt'))

# 2. Create a method that gets a file_name and a number as param and reads the numberth line of the file
def readline(file_name, number):
    f = open(file_name)
    result = f.readlines()[number-1].rstrip()
    return result

#print(readline('texts/zen_of_python.txt', 5))

# 3. Create a method that gets a long sentence as param and gives back the contained words in a list
def words(sentence):
    if sentence[-1:] == '.':
        sentence = sentence[:-1]
    list = sentence.split(' ')
    return list

#print(words("This is a try sentence"))

# 4. Create a method that gets a list of words and creates a sentence with the words separated by spaces
def sentence(words):
    sen = ''
    for i in words:
        sen += i + ' '
    sen = sen[:-1] + '.'
    return sen

# 5. Create a method that gets a string and gives back the character codes in a list
def char_codes(string):
    return [ord(i) for i in string]

# 6. Create a method that gets a list of integers and gives back a string which characters are created from the numbers used as character codes
def string(char_codes):
    string = ''
    for i in char_codes:
        string += chr(i)
    return string
