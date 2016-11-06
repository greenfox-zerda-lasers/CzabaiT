
def search_palindromes(string):
    # string expansion for handling 'out of index error'
    # when first/last letter is also a part of palindrome and loop searches for previous/next element
    string = "~" + string + "~"
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



print(search_palindromes('goddog goat dad duck doooodle neveroomoor'))