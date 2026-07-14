"""
Problem 16: Print the multiplication table of a given number.
"""

n = int(input("Enter num : "))

print(f"\n--- Multiplication Table of {n} ---")

for i in range(1, 11):
    
    result = n * i
    
    print(f"{n} * {i} = {result}")
