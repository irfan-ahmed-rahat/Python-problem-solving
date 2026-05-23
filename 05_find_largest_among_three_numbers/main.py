"""
Problem 5: Find the largest among three numbers.
"""

# Take three inputs from the user
num_1 = int(input("Enter first num: "))
num_2 = int(input("Enter second num: "))
num_3 = int(input("Enter third num: "))

# Check if num_1 is the largest
if num_1 >= num_2 and num_1 >= num_3:
    print(f"{num_1} is larger")

# Check if num_2 is the largest
elif num_2 >= num_1 and num_2 >= num_3:
    print(f"{num_2} is larger")

# If none of the above, num_3 is the largest
else:
    print(f"{num_3} is larger")
