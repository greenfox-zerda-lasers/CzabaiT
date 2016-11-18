import texts
import sys

class Todo:

    available_modes = ['-l', '-a', '-r', '-c']

    # initialization

    def __init__(self):
        self.inp = sys.argv
        self.inp_len = len(sys.argv)

        self.usage()

    # list operations & checkers

    def list_operations(self, operation, line=""):
        with open("todo_list.txt", operation) as file:
            if operation == "r":  #read
                return file.read().splitlines()
            elif operation == "w":  #new file
                file.write(line)
            elif operation == "a":  #add t odo
                file.write(line + "\n")

    def list_exist_checker(self):
        try:
            self.list_operations("r")
        except FileNotFoundError:
            self.list_operations("w")

    def list_empty_checker(self):
        list_chars_number = len(open("todo_list.txt").read())
        if list_chars_number == 0:
            print(texts.empty_list)
            sys.exit()

    def list_modify_argument_checker(self):
        list_lines_number = len(open("todo_list.txt").readlines())
        try:
            todo_number = int(self.inp[2])
            if todo_number <= 0 or todo_number > list_lines_number:
                print(texts.out_index)
                sys.exit()
        except IndexError:
            print(texts.no_index)
            sys.exit()
        except ValueError:
            print(texts.not_number)
            sys.exit()


# modes

    def mode_list(self):
        self.list_exist_checker()
        self.list_empty_checker()

        text = self.list_operations("r")
        number = 1
        for line in text:
            line_list = line.split(';')
            if line_list[0] == "unchecked":
                print("{0} - [ ] {1}".format(number, line_list[1]))
            elif line_list[0] == "checked":
                print("{0} - [x] {1}".format(number, line_list[1]))
            number += 1

    def mode_add(self):
        self.list_exist_checker()
        self.todo_description = " ".join(self.inp[2:])   #input t odo description part concatenation
        self.list_operations("a", "unchecked;" + self.todo_description)

    def mode_remove(self):
        self.list_exist_checker()
        self.list_empty_checker()
        self.list_modify_argument_checker()

        text = self.list_operations("r")
        f = open("todo_list.txt", "w")
        for line in range(0, len(text)):
            if line != int(self.inp[2]) - 1:  # 1 difference between countings
                f.write(text[line] + "\n")
        f.close()

    def mode_checked(self):
        self.list_exist_checker()
        self.list_empty_checker()
        self.list_modify_argument_checker()

        text = self.list_operations("r")
        f = open("todo_list.txt", "w")
        for line in range(0, len(text)):
            if line == int(self.inp[2]) - 1:  # 1 difference between countings
                new_line = "".join(text[line].split(';')[1:])
                f.write("checked;" + str(new_line) + "\n")
            else:
                f.write(text[line] + "\n")
        f.close()

# main flow

    def usage(self):
        if self.inp_len == 1:
            print(texts.usage)
        else:
            self.mode_select()

    def valid_mode(self):
        if self.inp[1] in self.available_modes:
            return self.inp[1]
        else:
            print(texts.argument_error)
            sys.exit()

    def mode_select(self):
        self.mode = self.valid_mode()
        if self.mode == '-l':
            self.mode_list()
        elif self.mode == '-a':
            self.mode_add()
        elif self.mode == '-r':
            self.mode_remove()
        elif self.mode == '-c':
            self.mode_checked()

todo = Todo()

