import math

def expNeeded(level):
    total = 0
    for i in range(1, level):
        
        total += math.floor(i + 300 * pow(2, i / 7.0))
    return math.floor(total / 4)

print(expNeeded(99))
