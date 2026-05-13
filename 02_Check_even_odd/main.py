

# Problem 2: Check if a number is Even or Odd.


# Take input from the user and convert to integer
num = int(input("Enter a number: "))

# Check if the remainder is 0 when divided by 2
if num % 2 == 0:
    print("Number is even")

# If the remainder is not 0, it must be odd
else:
    print("Number is odd")
