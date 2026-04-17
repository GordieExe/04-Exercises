def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

import math

test_values = [0, 1, 3, 5, 7, 10]

for v in test_values:
    print(v, factorial(v), math.factorial(v))
