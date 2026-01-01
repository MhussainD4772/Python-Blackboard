first_name = "Mohammed Hussain"
last_name = "Syed"

print(first_name + " " + last_name)


# =============================


nums = [10, 20, 30]
print(nums[0], nums[2])

# =============================

nums = [10, 20, 30]

for n in nums:
    print(n)

#=============================

nums = [10, 15, 20, 25]

for n in nums:
    if n > 15:
        print(n)


# =============================

nums = [5, 12, 10, 18, 7, 20]

for n in nums:
    if n < 10:
        print(f"{n} small")
    elif 10 <=n <= 15:
        print(f"{n} medium")
    else:
        print(f"{n} large")
    

