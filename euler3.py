from math import sqrt

rf_n = 600851475143
primes = [2]


def is_prime(n):
    if n > 1:
        if n == 2:
            return True
        for i in range(3, int(sqrt(n) + 1), 2):
            if n % i == 0:
                return False
        return True
    return False


def get_primes(n):
    while True:
        if is_prime(n):
            yield n
        n += 2


def euler():
    for n_p in get_primes(3):
        if n_p < 1000:
            primes.append(n_p)
        else:
            print(primes)
            return


# euler()

def largest_prime(n):
    i = 2  # first prime
    while i * i <= n:  # as long as i*i doesnt get to n you wont have the largest number divided
        if n % i:  # check whether n is dividable by i without rest value
            i += 1  # incrementing value if it is, we need to get to the primes!
        else:
            n //= i  # n = n // i, now n is the prime that was i
    return n


print(largest_prime(rf_n))
