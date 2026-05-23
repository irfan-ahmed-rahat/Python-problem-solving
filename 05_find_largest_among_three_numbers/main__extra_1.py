num_1 = int(input("Enter first num: "))
num_2 = int(input("Enter second num: "))
num_3 = int(input("Enter third num: "))

# সবচেয়ে বড় শর্ত: তিনটিই সমান কি না, সবার আগে চেক করতে হবে
if num_1 == num_2 == num_3:
    print(f"{num_1}, {num_2} and {num_3} all are equal")

# এরপর চেক করব কোনো একটি সংখ্যা সবার চেয়ে বড় কি না
elif num_1 > num_2 and num_1 > num_3:
    print(f"{num_1} is larger")

elif num_2 > num_1 and num_2 > num_3:
    print(f"{num_2} is larger")

elif num_3 > num_1 and num_3 > num_2:
    print(f"{num_3} is larger")

# এরপর চেক করব যেকোনো দুটি সমান কি না (এবং তারা কি তৃতীয়টির চেয়ে বড়?)
elif num_1 == num_2:
    print(f"{num_1} and {num_2} are equal and largest")

elif num_1 == num_3:
    print(f"{num_1} and {num_3} are equal and largest")

elif num_2 == num_3:
    print(f"{num_2} and {num_3} are equal and largest")
