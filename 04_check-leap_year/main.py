"""
Problem 4: Check whether a given year is a leap year.
"""

# Take year input from the user
year = int(input("Enter a year: "))

# Check if the year is divisible by 400 (Century leap year)
if year % 400 == 0:
    print(f"{year} is a leap year")

# Check if the year is divisible by 100 (Century non-leap year)
elif year % 100 == 0:
    print(f"{year} is not a leap year")

# Check if the year is divisible by 4 (Normal leap year)
elif year % 4 == 0:
    print(f"{year} is a leap year")

# If none of the above, it's not a leap year
else:
    print(f"{year} is not a leap year")
