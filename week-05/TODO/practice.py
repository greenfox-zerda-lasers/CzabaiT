import sys
import texts

"""
def list_operations(list_mode, line=""):
    file = open("todo_list.txt", list_mode)
    if list_mode == "r":
        return file.read().splitlines()
    elif list_mode == "w":
        file.write(line)
    elif list_mode == "a":
        file.write(line)

print(list_operations("a", "béluska"))
"""
"""
for line in text:
    line_list = line.split(';')
    if line_list[0] == "unchecked":
        print("[ ] " + line_list[1])
    elif line_list[0] == "checked":
        print("[x] " + line_list[1])
"""
"""
lista = ['1', '2']

def list_modify_argument_checker(lista):
    list_lines_number = len(open("todo_list.txt").readlines())
    try:
        todo_number = int(lista[3])
        if todo_number <= 0 or todo_number > list_lines_number:
            print(texts.out_index)
            sys.exit()
    except IndexError:
        print(texts.no_index)
        sys.exit()
    except ValueError:
        print(texts.not_number)
        sys.exit()

list_modify_argument_checker(lista)
"""

f = open("todo_list.txt", "r")
text = f.read().splitlines()
f.close()
print(text)

f = open("todo_list.txt", "w")
for line in range(0, len(text)):
    if line == 1 - 1:  # 1 difference between countings
        new_line = "".join(text[line].split(';')[1:])
        print(new_line)
        if line == len(text) - 1:  # last line without new line char
            f.write("checked;" + str(new_line))
        else:
            f.write("checked;" + str(new_line) + "\n")
    else:
        if line == len(text) - 1:
            f.write(text[line])
        else:
            f.write(text[line] + "\n")
