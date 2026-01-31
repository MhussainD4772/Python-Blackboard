nums = [4, 4, 6, 6, 6, 8, 9, 9]

seen = {}
list = []

for n in nums:
    if n in seen:
        seen[n] += 1
    else:
        seen[n] = 1

for ch, val in seen.items():
    if val % 2 == 1:
        list.append(ch)
# print(list)

# =========================================>

nums = [10, 20, 30, 40, 50]

# for i in range(len(nums)):
    # print(f"Index {i} has value {nums[i]}")


# =========================================>

# nums = [5, 10, 15, 20, 25]

# for i in range(len(nums)):
#     if i % 2 == 0:
#         print(nums[i])
#     else:
#         print(nums[i] * 2)


# =========================================>

nums = [2, 4, 6, 8, 10]

running_total = 0

for i in range(len(nums)):
    if i % 2 == 0:
        running_total += nums[i]
    else:
        running_total -= nums[i]
print(running_total)

# ==============================>












