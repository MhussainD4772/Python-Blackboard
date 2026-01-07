nums = [2, 4, 6, 8, 10, 3, 5]

even_num = []
odd_num = []

for num in nums:
    if num % 2 == 0:
        even_num.append(num)
    else:
        odd_num.append(num)
print(even_num)
print(odd_num)

# ==================================

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even_num = 0
odd_num = 0

for num in nums:
    if num % 2 == 0:
        even_num+=1
    else:
        odd_num+=1
print(even_num)
print(odd_num)

# ==================================

nums = [1, 2, 3, 4, 5]
result = []

for num in nums:
    if num % 2 == 0:
        result.append(num * num)
    else:
        result.append(num * num * num)
print(result)

# ==================================

nums = [1, 2, 2, 3, 3, 3, 4, 4, 5]

single_occurance = []
multiple_occurance = []

seen = {}

for n in nums:
    if n in seen:
        seen[n]+=1
    else:
        seen[n]=1

for num, value in seen.items():
    if value == 1:
        single_occurance.append(num)
    else:
        multiple_occurance.append(num)

print(single_occurance)
print(multiple_occurance)

# ==================================



