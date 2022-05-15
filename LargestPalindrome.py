
number = 0

for i in range(999, 100, -1):
    for j in range(i, 100, -1):
        a = i*j
        if a > number:
            a = str(a)
            if a == a[::-1]:
                number = int(a)

print(number)
