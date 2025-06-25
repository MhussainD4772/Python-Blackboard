#✅ Task #1 — Ask the user for their name and print:

name = input("What is your name ?")

print(f"Hello {name}!!") 

# ==================================================================>>>

#✅ Task #2 — Ask the user to enter two numbers, then print their sum.

first_number = int(input("What is you first numner ?"))
second_number = int(input("What is your second number ?"))

print(first_number + second_number)

# ==================================================================>>>

#🧠 Bonus Goal: Ask the user for three numbers, then add them using the sum() function and print the result.

first_number = int(input("First number ?"))
second_number = int(input("Second number ?"))
third_number = int(input("Third number ?"))

print(sum([first_number, second_number, third_number]))

# ==================================================================>>>

# ✅ Task #3 — Your Next Goal: Ask the user for a number.
#  If the number is greater than 10, print "Big number!" If it’s 10 or less, print "Small number."

number = int(input("Tell me the number that you wanna choose ?"))

if number > 10:
    print("Big number!")

else:
    print("Small number!")


# ==================================================================>>>

# ✅ Task #4 — Even or Odd Checker, Goal: Ask the user for a number. Print whether the number is even or odd.

number = int(input("Enter a number and python will tell you if it is odd or even !"))

if number % 2 == 0:
    print("Even number")
   
else:
    print("Odd number")

# ==================================================================>>>

#🌟 Creative Bonus Task — Even/Odd + Fun Fact, Goal: Enhance your even/odd program to include a fun fact based on the result.

number = int(input("Enter a number and python will tell you if it is odd or even !"))

if number % 2 == 0:
    print("Even number")
    print("Fun fact: Even numbers are perfectly divisible!")
   
else:
    print("Odd number")
    print("Odd numbers love being unique!")

# ==================================================================>>>









