
def gcd(number1, number2):
    n1 = number1
    n2 = number2

    while n2 != 0:
        remainder = n1 % n2
        n1 = n2
        n2 = remainder

    return n1


def lcm(number1, number2):
    return (number1*number2)/gcd(number1, number2)


smallest_positive_number = 1
for i in range(1, 20+1):
    smallest_positive_number = lcm(i, smallest_positive_number)

print("{} is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20.".format(int(smallest_positive_number)))
