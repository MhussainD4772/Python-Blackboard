nums = [1, 2, 3, 4]

result = []

for i in nums:
    total = i + i
    result.append(total)
print(result)

# #=============================

nums = [1, 2, 3, 4, 5]

result = []

for n in nums:
    if n % 2 == 0:
        result.append(n + n)
    else:
        result.append(n)
print(result)

# #============================

nums = [2, 5, 8, 1, 10, 3]

output = []

for n in nums:
    if n % 2 == 0:
        output.append(n * n)
print(output)

# #============================

nums = [3, 6, 9, 12, 15, 18]

result = 0

for n in nums:
    if n % 3 == 0:
        result+=1
print(result)

# #============================

nums = [4, 7, 2, 9, 10, 3, 8]

even_num = []
odd_num = []

even_count = 0
odd_count = 0

for n in nums:
    if n % 2 ==0:
        even_num.append(n)
        even_count+=1
    else:
        odd_num.append(n)
        odd_count+=1
print(even_num)
print(odd_num)
print(even_count)
print(odd_count)

# #==========================




