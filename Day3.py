# Warm-Up: Add Two Numbers (Again!) Goal: Ask the user for two numbers, then print the result as part of a complete sentence, like: "The total of 5 and 8 is 13."

num_1 = int(input("Give first number"))
num_2 = int(input("Give second number"))

print(f"The sum of {num_1} and {num_2} is {num_1 + num_2}")

# ==================================================================>>>

# Task 1 Goal Reminder: Ask the user for their age, and: If age < 13 → “You’re a kid. If age is 13–19 → “You’re a teenager.” If age is 20+ → “You’re an adult.”

user_age = int(input("Please tell us your age ?"))

if user_age < 13:
    print("You're a kid.")
elif user_age >= 13 and user_age <= 19:
    print("You're a teenager.") 
else:
    print("You're an adult.")

# ==================================================================>>>

#Task 2: Movie Ticket Price Checker, Goal: Ask the user for their age, and based on that, print the ticket price: Age under 4: Free ticket Age 4 to 12: $10 ticket Age 13 and above: $15 ticket.

age = int(input("Please enter your age here! "))

if age < 4:
    print("Hello champ your ticket is free")
elif 4 <= age <= 12:
    print("Hello the ticket price for you will be 10 dollars")
else:
    print("Hello the ticket price for you will be 15 dollars")

# ==================================================================>>>


#Task #3: Number Classifier Goal: Ask the user to enter any number. Then print out: "Positive number" if it’s greater than 0 "Negative number" if it’s less than 0 "Zero" if it’s exactly 0

number = int(input("Please enter your number here! "))

if number > 0:
    print("Positive Number")
elif number < 0:
    print("Negative number")
else:
    print("Zero")


# ==================================================================>>>


# 🌶️ Day 3 – Bonus Challenge: Grade Feedback System, Goal: Ask the user to enter their exam score (0–100).
# Then print feedback based on the score:
# 90 and above → "A – Excellent!"
# 80 to 89 → "B – Great job!"
# 70 to 79 → "C – Good effort."
# 60 to 69 → "D – Needs improvement."
# Below 60 → "F – You can do better next time."

exam_score = int(input("Enter your marks here! "))

if exam_score >= 90:
    print("A - Excellent!")
elif 80 <= exam_score <= 89:
    print("B – Great job!")
elif 70 <= exam_score <= 79:
    print("C – Good effort.")
elif 60 <= exam_score <= 69:
    print("D – Needs improvement.")
else:
    print("F – You can do better next time.")


# ==================================================================>>>






