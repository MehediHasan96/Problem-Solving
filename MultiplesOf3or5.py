def multiple(n):
    data = []
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            data.append(i)

    sum = 0
    for add in data:
        sum += add
    print("Sum of all multiples of 3 or 5 below {} is : {}".format(n, sum))


multiple(1000)


