#!/usr/bin/python3
import sys

# Function description:
# This function calculates the factorial of a given number 'n' recursively.
# The factorial of a number is the product of all positive integers less than or equal to that number.
# The base case is when n is 0, where the factorial is defined as 1.

# Parameters:
# n (int): The number for which the factorial is to be calculated. It must be a non-negative integer.

# Returns:
# int: The factorial of the number 'n'. If n is 0, it returns 1; otherwise, it recursively multiplies
# the number 'n' with the factorial of (n-1) until the base case is reached.

def factorial(n):
    if n == 0:
        return 1  # Base case: the factorial of 0 is 1
    else:
        return n * factorial(n-1)  # Recursive case: n * factorial(n-1)

# Read the input from the command line arguments and calculate the factorial
f = factorial(int(sys.argv[1]))
# Print the result
print(f)
