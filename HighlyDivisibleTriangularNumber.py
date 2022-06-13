import math


def get_divisor(n):
    factor = 2
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            if i ** 2 == n:
                factor += 1
            else:
                factor += 2
    return factor


triangular = 0
i = 0

while True:
    i += 1
    triangular += i
    divisor = get_divisor(triangular)
    if divisor > 500:
        print(triangular)
        break
