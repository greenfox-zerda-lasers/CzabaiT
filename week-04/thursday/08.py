# 8. Given a string, compute recursively a new string where all the 'x' chars have been removed.

def recursive(string):
    if not string:
        return ''

    if string[0] == 'x':
        return '' + recursive(string[1:])

    return string[0] + recursive(string[1:])

print(recursive('xamár'))