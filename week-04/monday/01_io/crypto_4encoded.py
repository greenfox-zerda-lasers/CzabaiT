# Create a method that decrypts texts/encoded_zen_lines.txt
def decrypt(file_name):
    result = ''
    with open(file_name) as fin:
        for line in fin:
            if line != '\n':
                for i in range(len(line)-1):
                    if line[i] == ' ':
                        result += ' '
                    else:
                        j = ord(line[i]) - 1
                        result += chr(j)
                result += '\n'
            else:
                result += line
    return result

print(decrypt('texts/encoded_zen_lines.txt'))
