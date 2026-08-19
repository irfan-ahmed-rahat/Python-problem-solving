"""
Problem 23: Check whether a number is an Armstrong number or not.
(Considering 3-digit numbers)
"""

num = int(input("Enter a 3-digit number: "))

original_num = num

total_sum = 0

while num > 0:
    
    digit = num % 10
    
    total_sum = total_sum + (digit ** 3)
    
    num = num // 10

if total_sum == original_num:
    print(f"{original_num} is an Armstrong number!")
else:
    print(f"{original_num} is not an Armstrong number.")
