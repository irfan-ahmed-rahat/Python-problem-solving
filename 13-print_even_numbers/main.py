"""
Problem 13: Print all even numbers from 1 to 100.
"""

# Loop from 1 (or 2) up to 100
for i in range(2, 101):
    
    # Check if the number is strictly divisible by 2
    if i % 2 == 0:
        print(i)
