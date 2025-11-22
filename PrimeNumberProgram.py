#A console application that generates prime numbers and checks for primality.
import Prime_testing_Algm as prime_test
import sieve_of_atkins as sieve_atkins
import SOE_timer as sieve_eratimer 
def display_menu():
    print("Prime Number Program")
    print("1. Generate Prime Numbers via Sieve of Eratosthenes")
    print("2. Generate Prime Numbers via Sieve of Atkin")
    print("3. Check Primality of a Number")
    print("4. Exit")

def option_one_action():
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the ending number: "))
    primes, elapsed = sieve_eratimer.primes_in_range_with_time(start, end)
    print(f"\nThere are {len(primes)} prime numbers in the interval [{start}, {end}]:")
    print(primes)
    print(f"\nExecution time: {elapsed:.6f} seconds")

def option_two_action():
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the ending number: "))
    primes, elapsed = sieve_atkins.primes_in_range_with_time(start, end)
    print(f"\nThere are {len(primes)} prime numbers in the interval [{start}, {end}]:")
    print(primes)
    print(f"\nExecution time: {elapsed:.6f} seconds")