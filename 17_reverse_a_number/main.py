"""
Problem 17: Reverse a given number.
"""

# ধাপ ১: ইনপুট নেওয়া
num = int(input("enter digit : "))

# ধাপ ২: নতুন সংখ্যা রাখার জন্য একটি খালি বাক্স
reverse = 0

# ধাপ ৩: লুপ চলবে যতক্ষণ num এর মান 0 এর চেয়ে বড় থাকে
while num > 0:
    
    # ধাপ ৪: শেষের ডিজিটটি আলাদা করা
    digit = num % 10
    
    # ধাপ ৫: নতুন বাক্সে সংখ্যাটি সাজানো (reverse-কে 10 দিয়ে গুণ করে জায়গা বানানো)
    reverse = (reverse * 10) + digit
    
    # ধাপ ৬: আসল সংখ্যা থেকে শেষের ডিজিটটি বাদ দিয়ে আপডেট করা
    num = num // 10

# ধাপ ৭: লুপের বাইরে এসে রেজাল্ট প্রিন্ট করা
print(f"The reversed number is: {reverse}")
