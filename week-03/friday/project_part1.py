
def create_palindrome(string):
    pali_string = string
    for i in range(len(string)-1,-1,-1):
        pali_string += string[i]
    return pali_string

print(create_palindrome('pear'))