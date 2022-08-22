def longest_collatz_sequence(n):
    number = [0, 1, 2]
    for i in range(3, n):
        temp = i
        count = 0
        while True:
            if temp % 2 == 0:
                temp = temp // 2
            else:
                temp = 3 * temp + 1
            count += 1

            if temp < i:
                number.append(count + number[temp])
                break
    return number.index(max(number))


lcs = longest_collatz_sequence(999999)
print(lcs)