"""
Problem 9: Check whether three angles can form a valid triangle.
"""

value_1 = float(input("Enter Your Value 1: "))
value_2 = float(input("Enter your value 2: "))
value_3 = float(input("Enter your value 3: "))

total_sum = value_1 + value_2 + value_3

if total_sum == 180 and value_1 > 0 and value_2 > 0 and value_3 > 0:
    print("This is a valid triangle")
else:
    print("Not a valid triangle")
