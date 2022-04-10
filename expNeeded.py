import math

def expNeeded(level):
    total = 0
    if(level <= 99):
        for i in range(1, level):
            total += math.floor(i + 300 * pow(2, i / 7.0))
    else:
        return "Level greater than 99, this isn't RS3"
    return math.floor(total / 4)

print(expNeeded(25))
