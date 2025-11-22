#Sieve of Atkin Function
import time

def sieve_of_atkin(limit: int) -> list[int]:

#Return a list of all prime numers up to user imput using the Sieve of Atkins

    if limit < 2:
        return[]
    
    sieve = [False] * (limit + 1)
    sqrt_limit = int(limit**0.5) + 1
    for x in range(1, sqrt_limit):
        for y in range(1, sqrt_limit):
            n = 4 * x**2 + y**2
            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                sieve[n] ^= True
            n = 3 * x**2 + y**2
            if n <= limit and n % 12 == 7:
                sieve[n] ^= True
            n = 3 * x**2 - y**2
            if x > y and n <= limit and n % 12 == 11:
                sieve[n] ^= True

    for p in range(5, sqrt_limit):
        if sieve[p]:
            for k in range(p**2, limit + 1, p**2):
                sieve[k] = False

    primes = []
    if limit >= 2:
        primes.append(2)
    if limit >= 3:
        primes.append(3)
    primes.extend([p for p in range(5, limit + 1) if sieve[p]])

    return primes
    """Return a list of all prime numbers up to the specified limit using the Sieve of Atkin algorithm."""

def atkin_timed(limit):
    start_time = time.time()
    primes = sieve_of_atkin(limit)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Sieve of Atkin found {len(primes)} primes up to {limit} in {elapsed_time:.6f} seconds.")
    print(primes) 

if __name__ == "__main__":
    n = int(input("Generate primes up to: "))
    atkin_timed(n)
