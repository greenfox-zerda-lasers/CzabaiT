
def search_palindromes(string):

    pali_list = []

    for i in range(1,len(string)-2):
        if string[i] == string[i+1]:
            j = 1
            while string[i-j] == string[i+j+1]:
                pali_list.append(string[i-j:i+j+2])
                j += 1
        else:
            j = 1
            while string[i-j] == string[i+j]:
                pali_list.append(string[i-j:i+j+1])
                j += 1
    return pali_list



print(search_palindromes('dog goat dad duck doodle never'))