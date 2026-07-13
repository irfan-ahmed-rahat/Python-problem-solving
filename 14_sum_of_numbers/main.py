"""
Problem 14: Calculate the sum of numbers from 1 to n.
"""

n = int(input("Enter num: "))
total = 0

for i in range(1, n + 1):
    total = total + i
print(f"The total sum is: {total}")
