import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except:
    print("Unexpected error:", sys.exc_info()[0])