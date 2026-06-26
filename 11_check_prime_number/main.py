"""
Problem 11: Check whether a number is prime or not.
"""


num = int(input("Enter your number: "))

# Initially, assume the number is prime
is_prime = True

# Prime numbers are always greater than 1
if num > 1:
    # Loop from 2 to the number before 'num'
    for i in range(2, num):
        # If it is divisible by any number, it's not prime
        if num % i == 0:
            is_prime = False
            break
else:
    is_prime = False

# Final decision output
if is_prime == True:
    print(f"{num} is prime")
else:
    print(f"{num} is not prime")
