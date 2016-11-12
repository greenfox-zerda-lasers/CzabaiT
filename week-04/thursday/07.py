# 7. Given a string, compute recursively (no loops) a new string where all the
# lowercase 'x' chars have been changed to 'y' chars.

def recursive(string):
    if not string:
        return ''

    if string[0] == 'x':
        return 'y' + recursive(string[1:])

    return string[0] + recursive(string[1:])

print(recursive('bélax'))

#print('béla'[2])

