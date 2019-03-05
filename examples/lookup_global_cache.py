import math

def compute_cache():
    total = 0
    sin = math.sin
    for x in range(1000):
        total += sin(x)
    return total

compute_cache()