# Take input from the user and convert to integer
num_1 = int(input("Enter your first number: "))
num_2 = int(input("Enter your second number: "))

# Check if the first number is greater
if num_1 > num_2:
    print("First number is larger")

# Check if both numbers are equal
elif num_1 == num_2:
    print("Both are equal")

# If none of the above conditions are true, the second number must be larger
else:
    print("Second number is larger")
