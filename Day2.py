# ✅ Task #1 — Basic Math Input Goal: Ask the user to enter two numbers, then print their sum.

first_number = int(input("First Number ?"))
second_number = int(input("Second Number ?"))

print("The sum is:", first_number + second_number)

# ==================================================================>>>

# ✅ Task #2 — Personalized Math Result, Goal: Ask the user for their name, then ask for two numbers, and finally print a personalized message like: "Hey Mohammed, the total of 5 and 8 is 13."

name = input("What's your name ?")
first_number = int(input("Enter first number !"))
second_number = int(input("Enter second number !"))

print(f"Hey {name}, the total of {first_number} and {second_number} is {first_number + second_number}")

# ==================================================================>>>

# ✅ Task #3: Three Number Average. Goal: Ask the user for three numbers, then calculate and print their average.

first_number = float(input("Enter first number."))
second_number = float(input("Enter second number."))
third_number = float(input("Enter third number."))

mean = (first_number + second_number + third_number) / 3.0
print(f"The mean of {first_number}, {second_number}, {third_number} is : {mean}")

# ==================================================================>>>

# ✅ Task #4: Conditional Mean Printer. Goal: Ask the user to enter three numbers. Calculate the mean as before, but only print the mean if it is greater than 10. If it’s 10 or below, print: "Mean is too small to display."

num_1 = float(input("Enter first number."))
num_2 = float(input("Enter second number."))
num_3 = float(input("Enter third number."))

mean = (num_1 + num_2 + num_3) / 3.0

if mean > 10:
    print(f"The mean is {mean}")

else:
    print("Mean is too small to display.")

# ==================================================================>>>

# 🌟 Creative Bonus Task: Weighted Average Calculator. Goal: Ask the user for 3 exam scores, and then ask for a weight (0–1) for each exam. Then calculate and print the weighted average.

exam_score_1 = float(input("Enter exam 1 score."))
weight_1 = float(input("Enter weight 1."))

exam_score_2 = float(input("Enter exam 2 score."))
weight_2 = float(input("Enter weight 2."))

exam_score_3 = float(input("Enter exam 3 score."))
weight_3 = float(input("Enter weight 3."))

weighted_avg = (exam_score_1 * weight_1) + (exam_score_2 * weight_2) + (exam_score_3 * weight_3)
print(f"The weighted average is {weighted_avg: 2f}")


# ==================================================================>>>


