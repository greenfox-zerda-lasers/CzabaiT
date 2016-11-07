# Create a method that decrypts texts/reversed_zen_order.txt
def decrypt(file_name):
    result = ''
    fr = open(file_name)
    rev_file = fr.read()
    fr.close()

    for line in rev_file.splitlines()[::-1]:
        result += line + '\n'
    return(result)
