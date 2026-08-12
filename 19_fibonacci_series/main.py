"""
Problem 19: Print the Fibonacci series up to n terms.
"""

# ধাপ ১: ইউজারের কাছ থেকে ইনপুট 
num = int(input("Enter how many terms you want: "))

# ধাপ ২: ফিবোনাচির শুরুর দুটি ফিক্সড সংখ্যা
num1 = 0
num2 = 1

print(f"\nFibonacci Series up to {n} terms:")

# ধাপ ৩: লুপ 
for i in range(num): # range(1 ,num+1) দিলেও হবে
    
    # ধাপ ৪: প্রথম সংখ্যাটি প্রিন্ট  
    print(num1, end=" ")
    #end=" " দিলে সংখ্যাগুলো নিচে নিচে প্রিন্ট না হয়ে পাশাপাশি স্পেস দিয়ে প্রিন্ট হয়)।
    
    # ধাপ ৫: আগের দুটি সংখ্যা যোগ করে নতুন সংখ্যা তৈরি 
    next_num = num1 + num2
    
    # ধাপ ৬: মানগুলো এক ঘর করে সামনে এগিয়ে 
    num1 = num2
    num2 = next_num
