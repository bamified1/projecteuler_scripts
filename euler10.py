from math import sqrt

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
        if n_p < 2000000:
            primes.append(n_p)
        else:
            return


euler()

print(sum(primes))
