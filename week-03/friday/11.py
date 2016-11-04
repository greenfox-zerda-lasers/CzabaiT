# Create a function that prints a diamond like this:
#       *
#      ***
#     *****
#    *******
#   *********
#  ***********
#   *********
#    *******
#     *****
#      ***
#       *
#
# It should take a number as parameter that describes how many lines the diamond has


def really_triangle(number):
    # based 5. line:
    # STEP 1: width:(chars in line): 11 -> !! 2*number-1 !! number=given parameter
    # STEP 2: stars: 9 -> !! 2*i-1 !! i=line number
    # STEP 3: spaces: 2 -> 11-9 -> (2*number-1)-(2*i-1)
    # STEP 4: 1 sided spaces: !! (11-(2*i-1))/2 !!

    # line-up:  1 sided spaces  // stars // 1 sided_spaces
    # first for: increment part till 11 stars
    # second for: decrement part from 9 stars
    width = (2 * number) - 1
    for i in range(1, number+1):
        print(int((width - (2 * i - 1)) / 2) * ' ', int(2 * i - 1) * '*', int((width - (2 * i - 1)) / 2) * ' ')
    for i in range(number-1, 0, -1):
        print(int((width - (2 * i - 1)) / 2) * ' ', int(2 * i - 1) * '*', int((width - (2 * i - 1)) / 2) * ' ')

really_triangle(6)


