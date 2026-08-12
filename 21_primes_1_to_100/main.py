"""
Problem 21: Print all prime numbers between 1 and 100.
"""

print("Prime numbers between 1 and 100 are:")

# বাইরের লুপ: ২ থেকে ১০০ পর্যন্ত প্রতিটি সংখ্যা চেক করার জন্য
for num in range(2, 101):
    
    # শুরুতে ধরে নিচ্ছি সংখ্যাটি প্রাইম
    is_prime = True

    # ভেতরের লুপ: সংখ্যাটিকে ২ থেকে তার আগের সংখ্যা পর্যন্ত ভাগ করে দেখা
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break # ভাগ গেলে এটি আর প্রাইম নয়, তাই লুপ ভেঙে বেরিয়ে আসো
            
    # ভেতরের লুপের চেকিং শেষে যদি প্রাইম থাকে, তবে সেটি প্রিন্ট করো
    if is_prime:
        print(num, end=" ")
