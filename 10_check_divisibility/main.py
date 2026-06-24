"""
Problem 10: Check whether a number is divisible by 5 and 11 or not.
"""

value = int(input("Enter Your Value: "))

if value % 5 == 0 and value % 11 == 0:
    print(f"{value} is divisible by both 5 and 11")
    
else:
    print(f"{value} is not divisible by both 5 and 11")
