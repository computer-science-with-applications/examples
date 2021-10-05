from primes import is_prime
from mersenne import is_mersenne_prime, is_power_of_two

if __name__ == "__main__":
    n = input("Enter a number: ")

    n = int(n)

    if not is_prime(n):
        print(f"{n} is not a prime number.")
    else:
        p = is_power_of_two(n+1)
        if p is not None:
            if is_mersenne_prime(n):
                print(f"{n} is a double Mersenne prime: both {n} and 2^{n}-1 are Mersenne primes.")
            else:
                print(f"{n} is a Mersenne prime ({n} == 2^{p}-1)")
        else:
            if is_mersenne_prime(n):
                print(f"{n} is a prime number, but not a Mersenne prime (however, 2^{n}-1 is a Mersenne prime).")
            else:
                print(f"{n} is a prime number, but not a Mersenne prime (and neither is 2^{n}-1).")



