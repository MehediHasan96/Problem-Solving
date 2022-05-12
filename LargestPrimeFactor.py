def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


number = 600851475143

prime_factor = [1]


def largest_prime_factor(num):
    for i in range(2, num//2+1):
        if num % i == 0:
            if is_prime(i):
                prime_factor.append(i)


largest_prime_factor(number)
print("The largest prime factor of the number {} is {}".format(number, max(prime_factor)))
