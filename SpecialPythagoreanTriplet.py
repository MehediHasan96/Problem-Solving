import math

for a in range(1, 1000):
    for b in range(1, 1000):
        c = math.sqrt(a*a + b*b)
        if a < b < c and a+b+c == 1000:
            product = a*b*c

print(int(product))

