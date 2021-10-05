import primes
import math


def is_mersenne_prime(p):
    if p == 2:
        return True

    s = 4
    m = 2**p - 1
    for _ in range(p-2):
        s = ((s*s)-2) % m

    return s == 0


def is_power_of_two(n):
    # Can n be expressed as 2^m?
    m = math.log2(n)

    if m.is_integer() and 2**int(m) == n:
        return int(m)
    else:
        return None


def print_mersenne_primes(max_p):
    i = 1
    for p in range(max_p):
        if not primes.is_prime(p):
            continue
        if is_mersenne_prime(p):
            print(f"M{i} is {p}")
            i += 1
