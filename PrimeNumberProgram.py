#A console application that generates prime numbers and checks for primality.
import time
import math
import random

def sieve_of_eratosthenes(n):
    """
    Use the Sieve of Eratosthenes to find all prime numbers between 2 and n, and return the list.
    """
    if n < 2:
        return []

    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False

    p = 2
    while p * p <= n:
        if is_prime[p]:
            # Starting from p*p, cross out multiples of p.
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False
        p += 1

    return [i for i in range(2, n + 1) if is_prime[i]]


def primes_in_range_with_time(start, end):
    """
    Find prime numbers within the [start, end] interval and record the elapsed time.
    Return (primes_list, elapsed_seconds)
    """
    if start > end:
        return [], 0.0
    # A lower bound less than 2 is meaningless; it is enforced to start from 2.
    if end < 2:
        return [], 0.0
    if start < 2:
        start = 2

    t0 = time.perf_counter()
    all_primes_up_to_end = sieve_of_eratosthenes(end)
    primes = [p for p in all_primes_up_to_end if p >= start]
    t1 = time.perf_counter()

    return primes, t1 - t0

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
    return primes, elapsed_time 

# List for generated or inputed test numbers
def list_Of_Numbers(the_list):
    test_Numbers = the_list




# Trail devision
def trail_Devision(n):
    if n<= 1:
        return False
    limit = int(math.sqrt(n)) + 1
    for i in range(2, limit):
        if n % i == 0:
            return False
    return True

def generate_test_cases(count, min_digits, max_digits):
    temp_list = []
    for _ in range(count):
        # Determine a random number of digits for size variation
        num_digits = random.randint(min_digits, max_digits)
        
        # Calculate the range for the random number
        min_val = 10**(num_digits - 1)
        max_val = (10**num_digits) - 1 
        
        # Generate the number and add it to the list
        number = random.randint(min_val, max_val)
        temp_list.append(number)

def run_Time_Tracker(A_List):
    for number in A_List:
        start_time = time.time()
        result = trail_Devision(number)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Number: {number}, Prime: {result}, Time taken: {elapsed_time:.10f} seconds")


def main():
    start = int(input("Please enter the starting number start："))
    end = int(input("Please enter the final number end："))

    primes, elapsed = primes_in_range_with_time(start, end)

    print(f"\nThere are {len(primes)} prime numbers in the interval [{start}, {end}]:")
    print(primes)
    print(f"\nExecution time: {elapsed:.6f} seconds")
    run_Time_Tracker(primes)

    n = int(input("Generate primes up to: "))
    primes_atkin, elapsed_atkin = atkin_timed(n)
    run_Time_Tracker(primes_atkin)

if __name__ == "__main__":
    main()