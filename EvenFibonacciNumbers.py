n = 4000000
n1 = 1
n2 = 2
sum = 0
count = 0

while count < n:
    if n1 % 2 == 0:
        sum += n1

    n3 = n1 + n2
    n1 = n2
    n2 = n3
    count += 1

print(sum)
