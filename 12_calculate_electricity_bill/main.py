"""
Problem 12: Calculate electricity bill based on unit consumption slabs.
"""

# Take the electricity unit input from the user
unit = float(input("Enter your unit: "))

# Calculate bill based on slabs
if unit <= 100:
    # First 100 units cost 5 TK per unit
    bill = unit * 5
else:
    # First 100 units at 5 TK + additional units at 10 TK
    bill = (100 * 5) + ((unit - 100) * 10)

# Print the final calculated bill
print(f"Your total bill is: {bill} TK")
