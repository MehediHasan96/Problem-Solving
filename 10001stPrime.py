def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def find_prime_number(num):
    count = 1
    num_prime = 0
    while num_prime < num:
        count += 1
        if is_prime(count):
            num_prime += 1
    return count


print("10001st prime number is {}".format(find_prime_number(10001)))

