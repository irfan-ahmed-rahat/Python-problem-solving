# Check if a user is eligible to vote based on age.


# Take age input from the user and convert to integer
age = int(input("Enter your age: "))

# Check if age is 18 or greater
if age >= 18:
    print("You are eligible to vote")

# If age is less than 18
else:
    print("You are not eligible to vote")
