"""
Problem 22: Calculate power using loop (e.g., 2^3 = 8).
"""

base = int(input("Enter your base number: "))
power = int(input("Enter your power number: "))

result = 1

for i in range(1, power + 1):
    
    result = result * base

print(f"{base} to the power of {power} is: {result}")
