 """
 Check whether a number is positive, negative, or zero.
"""

# Take a number as input from the user (using float to support decimals)
num = float(input("Enter your number: "))

# Check if the number is greater than zero
if num > 0:
    print(f"{num} is positive")

# Check if the number is less than zero
elif num < 0:
    print(f"{num} is negative")

# If it is neither greater nor less than zero, it must be zero
else:
    print("Number is 0")
