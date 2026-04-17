import math

def magnitude(x, y, z=0):
    return math.sqrt(x**2 + y**2 + z**2)

print(magnitude(3, 4))   
print(magnitude(1, 2, 2))   