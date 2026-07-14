"""
Problem 18: Check whether a number is a palindrome.
"""

# ধাপ ১: ইনপুট নেওয়া
num = int(input("enter digit : "))

# ধাপ ২: আসল সংখ্যাটিকে temp নামের একটি বাক্সে ব্যাকআপ রাখা
temp = num

# ধাপ ৩: উল্টানো সংখ্যা রাখার জন্য খালি বাক্স
reverse = 0

# ধাপ ৪: সংখ্যা উল্টানোর while লুপ
while num > 0:
    digit = num % 10
    reverse = (reverse * 10) + digit
    num = num // 10

# ধাপ ৫: ব্যাকআপ (temp) এবং উল্টানো সংখ্যা (reverse) সমান কি না চেক করা
if reverse == temp:
    print(f"{temp} is palindrome")
else:
    print(f"{temp} is not palindrome")
