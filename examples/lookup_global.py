import math

def compute():
    total = 0
    for x in range(1000):
        total += math.sin(x)
    return total

compute()