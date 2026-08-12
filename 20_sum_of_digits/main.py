"""
Problem 20: Calculate the sum of digits of a number.
"""

# ধাপ ১: ইউজারের কাছ থেকে ইনপুট নেওয়া
num = int(input("Enter a number to find the sum of its digits: "))

# আসল সংখ্যাটি সেভ করে রাখা (ফাইনাল প্রিন্টে দেখানোর জন্য)
original_num = num

# ধাপ ২: যোগফল জমানোর জন্য ভেরিয়েবল (মাটির ব্যাংক) তৈরি
total_sum = 0

# ধাপ ৩: লুপ চলবে যতক্ষণ num এর মান 0 এর চেয়ে বড় থাকে
while num > 0:
    
    # ধাপ ৪: শেষের ডিজিটটি আলাদা করা
    digit = num % 10
    
    # ধাপ ৫: আলাদা করা ডিজিটটিকে মাটির ব্যাংকে যোগ করা
    total_sum = total_sum + digit
    
    # ধাপ ৬: আসল সংখ্যা থেকে শেষের ডিজিটটি বাদ দিয়ে আপডেট করা
    num = num // 10

# ধাপ ৭: লুপের বাইরে এসে ফাইনাল যোগফল প্রিন্ট করা
print(f"The sum of the digits of {original_num} is: {total_sum}")
