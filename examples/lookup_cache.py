import math

def cache():
    sin = math.sin
    total = 0
    for x in range(1000):
        total += sin(x)
    return total

cache()