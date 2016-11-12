# 5. We have a number of bunnies and each bunny has two big floppy ears.
# We want to compute the total number of ears across all the bunnies
# recursively (without loops or multiplication).

def recursive(bunnies, floppy_ears):
    if bunnies == 1:
        return floppy_ears
    else:
        return floppy_ears + recursive(floppy_ears, bunnies-1)

print(recursive(17,5))