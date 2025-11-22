# Hello world
# How are you?
import math
import time
import random

# List for generated or inputed test numbers
test_Numbers = []

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
    for _ in range(count):
        # Determine a random number of digits for size variation
        num_digits = random.randint(min_digits, max_digits)
        
        # Calculate the range for the random number
        min_val = 10**(num_digits - 1)
        max_val = (10**num_digits) - 1 
        
        # Generate the number and add it to the list
        number = random.randint(min_val, max_val)
        test_Numbers.append(number)

def run_Time_Tracker():
    for number in test_Numbers:
        start_time = time.time()
        result = trail_Devision(number)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Number: {number}, Prime: {result}, Time taken: {elapsed_time:.10f} seconds")



