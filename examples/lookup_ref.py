import math

def compute():
    total = 0
    for x in range(1000):
        total += math.sin(x)
    return total


def compute_cache():
    sin = math.sin
    total = 0
    for x in range(1000):
        total += sin(x)
    return total