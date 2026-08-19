"""
Problem 24: Take unlimited inputs from user until they enter 0.
"""

print("Enter numbers (Enter 0 to stop):")

while True:
    
    num = int(input("Enter a number: "))
    
    if num == 0:
        print("You entered 0. Exiting the loop!")
        break 
        
    print(f"You entered: {num}")

print("Program ended successfully!")
