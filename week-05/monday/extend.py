
# Adds a and b, returns as result
def add(a, b):
    return a + b

# Returns the highest value from the three given params
def max_of_three(a, b, c):
    return max(a, b, c)

# Returns the median value of a list given as param
def median(pool):
    if len(pool) % 2 == 0:
        return (sorted(pool)[len(pool) // 2] + sorted(pool)[(len(pool) // 2) + 1]) / 2
    else:
        return sorted(pool)[len(pool) // 2]

# Returns true if the param is a vovel
def is_vovel(char):
    return char.lower() in 'aeiouúéáőűöüóí'

# Create a method that translates hungarian into the teve language
def translate(hungarian):
    teve = ''
    for i in hungarian:
        if is_vovel(i):
            teve += i + 'v' + i
        else:
            teve += i
    return teve
