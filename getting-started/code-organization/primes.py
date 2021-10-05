import math


def print_primes(max_n):
    for n in range(2, max_n+1):
        if is_prime(n):
            print(n)


def is_prime(n):
    # Directly check for 1, 2, and 3 (as well as
    # values less than 1)
    if n <= 1:
        return False
    elif n == 2 or n == 3:
        return True

    # Numbers greater than 3 that are divisible by 2 or 3
    # are not prime
    if n % 2 == 0 or n % 3 == 0:
        return False

    # We only check divisors of the form 6*k-1 and 6*k+1,
    # starting with k=1. To do this, we use a variable i
    # that will contain the value of 6*k, and we check
    # that value minus one and plus one in each iteration
    # of the loop (and increment i by 6 after each iteration)
    #
    # We also stop checking if 6k becomes larger than
    # the square root of n
    for i in range(6, math.ceil(math.sqrt(n)), 6):
        # Check if n is divisible by 6*k-1
        if n % (i-1) == 0:
            return False
        # Check if n is divisible by 6*k+1
        if n % (i+1) == 0:
            return False

    return True
