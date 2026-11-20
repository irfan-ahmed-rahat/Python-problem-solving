"""
Problem 25: Sum and Average of a List
Description: Calculate the total sum and average of all numbers in a list using a loop.
"""

numbers = [1, 2, 5, 8, 6]
total = 0

# Calculate the sum of all elements in the list
for num in numbers:
    total += num

# Count total elements and calculate the average
count = len(numbers)
average = total / count

# Display the result
print(f"List: {numbers}")
print(f"Total Sum: {total}")
print(f"Average: {average}")
