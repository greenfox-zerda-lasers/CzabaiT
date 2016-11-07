# Create a method that decrypts the texts/duplicated_chars.txt

def decrypt(file_name):
    result = ''
    with open(file_name) as fin:
        for line in fin:
            if line != '\n':
                for i in range(len(line)):
                    if i % 2 == 0:
                        result += line[i]
            else:
                result += line
    return result

