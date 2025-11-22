# -*- coding: utf-8 -*-
"""
Created on Wed Nov 19 14:11:37 2025

@author: 35746
"""

import time

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

    return primes, (t1 - t0)


if __name__ == "__main__":
    start = int(input("Please enter the starting number start："))
    end = int(input("Please enter the final number end："))

    primes, elapsed = primes_in_range_with_time(start, end)

    print(f"\nThere are {len(primes)} prime numbers in the interval [{start}, {end}]:")
    print(primes)
    print(f"\nExecution time: {elapsed:.6f} seconds")

