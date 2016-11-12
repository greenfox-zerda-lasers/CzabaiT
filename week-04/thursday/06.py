# 6. We have bunnies standing in a line, numbered 1, 2, ... The odd bunnies
# (1, 3, ..) have the normal 2 ears. The even bunnies (2, 4, ..) we'll say
# have 3 ears, because they each have a raised foot. Recursively return the
# number of "ears" in the bunny line 1, 2, ... n (without loops or
# multiplication).

def recursive(bunnies, even_ears, odd_ears):
    if bunnies == 1:
        return odd_ears
    else:
        if bunnies % 2 == 0:
            return even_ears + recursive(bunnies-1, even_ears, odd_ears)
        else:
            return odd_ears + recursive(bunnies - 1, even_ears, odd_ears)

print(recursive(5,2,3))