nums = [1, 2, 1, 3, 2, 1]

count = {}

for n in nums:
    if n in count:
        count[n] += 1
    else:
        count[n] = 1
# print(count)


# =======================================

# nums = [4, 5, 6, 5, 4, 3, 4]

# count = {}

# for n in nums:
#     if n in count:
#         count[n] += 1
#     else:
#         count[n] = 1

# for num, c in count.items():
#     if c > 1:
#         print(num)


# =======================================

nums = [2, 3, 2, 5, 3, 3, 4]

count = {}
max_num = 0

for n in nums:
    if n in count:
        count[n] += 1
    else:
        count[n] = 1

for num, c in count.items():
    if c > max_num:
        max_num = num
print(max_num)


# =======================================





