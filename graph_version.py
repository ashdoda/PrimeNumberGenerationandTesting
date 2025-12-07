import time
import math
import random
import matplotlib.pyplot as plt
import numpy as np


def generate_random_numbers(count, low=1, high=1_000_000_000):
    """
    Generate 'count' random integers between low and high (inclusive).
    """
    return [random.randint(low, high) for _ in range(count)]
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


def primes_up_to_with_time(n):
    """
    Return all primes from 1 to n (i.e., primes up to n)
    along with the elapsed time.
    """
    if n < 2:
        return [], 0.0

    t0 = time.perf_counter()
    primes = sieve_of_eratosthenes(n)
    t1 = time.perf_counter()

    return primes, (t1 - t0)

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
    return primes, elapsed_time 
def run_random_experiments(num_cases, low_n, high_n):
    """
    Generate random n values and time both Sieve of Eratosthenes
    and Sieve of Atkin on each.
    Returns: (n_values, eratosthenes_times, atkin_times)
    """
    # 1. Generate random test sizes
    n_values = generate_random_numbers(num_cases, low=low_n, high=high_n)
    n_values.sort()  # sort so the x-axis looks nicer

    eratosthenes_times = []
    atkin_times = []

    for n in n_values:
        # Time Eratosthenes
        _, t_erat = primes_up_to_with_time(n)
        
        # Time Atkin
        _, t_atkin = atkin_timed(n)

        eratosthenes_times.append(t_erat)
        atkin_times.append(t_atkin)

        print(f"n = {n:,} | Eratosthenes: {t_erat:.6f} s | Atkin: {t_atkin:.6f} s")

    return n_values, eratosthenes_times, atkin_times

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
    start_time = time.time()
    for number in A_List:
        result = trail_Devision(number)
        if result == False:
            print(f"Number: {number}, Prime: {result}")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Total Time taken for all numbers: {elapsed_time:.10f} seconds")

def plot_times_with_best_fit(n_values, erat_times, atkin_times):
    """
    Scatter-plot the runtimes and draw best-fit lines for each algorithm.
    """
    # Convert to numpy arrays for polyfit
    x = np.array(n_values, dtype=float)
    y_erat = np.array(erat_times, dtype=float)
    y_atkin = np.array(atkin_times, dtype=float)

    # Scatter plots
    plt.scatter(x, y_erat, label="Eratosthenes (data)")
    plt.scatter(x, y_atkin, label="Atkin (data)")

    # Best-fit line for Eratosthenes
    coef_erat = np.polyfit(x, y_erat, 1)   # degree-1 polynomial (line)
    fit_erat = np.polyval(coef_erat, x)
    plt.plot(x, fit_erat, linestyle="--", label="Eratosthenes (best fit)")

    # Best-fit line for Atkin
    coef_atkin = np.polyfit(x, y_atkin, 1)
    fit_atkin = np.polyval(coef_atkin, x)
    plt.plot(x, fit_atkin, linestyle="--", label="Atkin (best fit)")

    plt.xlabel("n (upper limit for primes)")
    plt.ylabel("Time (seconds)")
    plt.title("Runtime of Sieve of Eratosthenes vs Sieve of Atkin")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    print("Choose mode:")
    print("1) Manual single run")
    print("2) Random experiment + plot")

    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        # Existing behavior
        end = int(input("Please enter the final number end: "))
        primes, elapsed = primes_up_to_with_time(end)

        print(f"\nThere are {len(primes)} prime numbers in the interval [1, {end}]:")
        print(f"\nExecution time (Eratosthenes): {elapsed:.6f} seconds")
        run_Time_Tracker(primes)

        n = int(input("Generate primes up to (Atkin): "))
        primes_atkin, elapsed_atkin = atkin_timed(n)
        run_Time_Tracker(primes_atkin)

    elif choice == "2":
        # New random experiment mode
        num_cases = int(input("How many random test sizes do you want? "))
        low_n = int(input("Minimum n value: "))
        high_n = int(input("Maximum n value: "))

        n_values, erat_times, atkin_times = run_random_experiments(
            num_cases, low_n, high_n
        )

        # Plot the results with best-fit lines
        plot_times_with_best_fit(n_values, erat_times, atkin_times)

    else:
        print("Invalid choice. Exiting.")
        
if __name__ == "__main__":
    main()