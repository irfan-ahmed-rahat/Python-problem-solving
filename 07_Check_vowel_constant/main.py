"""
Problem 7: Check whether a character is a vowel or consonant.
"""


char = input("Enter your keyword: ")

if char in "aeiouAEIOU":
    print(f"{char} is a vowel")
  
else:
    print(f"{char} is not a vowel")
