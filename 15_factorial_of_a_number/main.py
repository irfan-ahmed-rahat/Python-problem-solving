"""
Problem 15: Calculate the factorial of a given number.
"""

n = int(input("Enter a number to find its factorial: ")) 

result = 1

for i in range(1, n + 1):
    
    result = result * i 

print(f"The factorial of {n} is: {result}")
