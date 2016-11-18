# write a function that takes a filename and returns the number of lines the
# file consists. It should return zero if the file not exists.

def file_line_counter(file):

    try:
        with open(file) as opener:
            text = opener.readlines()
            print(text)

        count = 0

        for _ in text:
            count += 1

        return count

    except FileNotFoundError:
        return 'zero'


#print(file_line_counter('text.txt'))