# 9. Given a string, compute recursively a new string where all the
# adjacent chars are now separated by a "*"

def recursive(string):
    if not string:
        return ''
    return string[0] + '*' + recursive(string[1:])

print(recursive('bélax'))