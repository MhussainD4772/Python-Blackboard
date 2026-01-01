# Day 4 – Task #1: Countdown Timer, Goal: Ask the user for a number, and then count down to 0, printing each number on a new line.

number = int(input("Enter your number here! "))

while number >= 0:
    print(number)
    number -=1
print("Blast off!")


# ==================================================================>>>

# Task #2: Secret Word Guesser Goal: Create a program that keeps asking the user to guess a secret word until they get it right.
# The word should be hardcoded by you (e.g., "python").
# If the guess is wrong → say "Try again!"
# If the guess is correct → say "Correct! You're in." and stop the loop.

answer = "python"
guess = "Enter the secret word here: "
print(guess)

while guess == answer:
    print("Correct! You're in.")
else:
    print("Try again!")


# ==================================================================>>>

 
#Task #3: Multiplication Table Printer Goal: Ask the user for a number, and then print the multiplication table for that number from 1 to 10.
# 🧠 Example:
# Enter a number: 3  
# 3 x 1 = 3  
# 3 x 2 = 6  
# 3 x 3 = 9  
# ...  
# 3 x 10 = 30

num = int(input("Enter number here! "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")


# ==================================================================>>>

# ✅ Task #4: Sum Until Zero. Goal: Ask the user to enter numbers one at a time, and keep a running total. stop asking when they enter 0, and then print the total sum.


total = 0
num = int(input("Enter number here! "))

while num != 0:
    total += num
    num = int(input("Enter number here! "))

print(f"The total is {total}")

# ==================================================================>>>

# Task #5: Keep Track of the Largest Number Goal: Ask the user to enter numbers one at a time. Keep asking until they enter 0. At the end, print the largest number they entered (not counting the 0)

largest = None

num = int(input("Enter a number (0 to stop): "))

while num != 0:
    if largest is None or num > 0 :
        largest = num
    num = int(input("Enter a number (0 to stop): "))

if largest is not None:
    print(f"Largest number is: {largest}")
else:
    print("No valid numbers were entered.")



# ==================================================================>>>

    































