# Create a method that decrypts texts/reversed_zen_lines.txt
def decrypt(file_name):
    result = ''
    with open(file_name) as fin:
        for line in fin:
            # [-2::-1] because this way last character '\n' doesn't get to the line front
            result += line[-2::-1] +'\n'
    return result
