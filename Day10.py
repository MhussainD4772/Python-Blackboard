s = "banana"

seen = {}

for i in s:
    if i in seen:
        seen[i] += 1
    else:
        seen[i] = 1
print(seen)

# =============================

s = "swiss"

seen = {}

for i in s:
    if i in seen:
        seen[i] += 1
    else:
        seen[i] = 1

for i in s:
    if seen[i] == 1:
        print(i)
        break

# =============================


s = "programming"

seen = {}

for i in s:
    if i in seen:
        seen[i] +=1
    else:
        seen[i] = 1
print(seen)

for i in s:
    if seen[i] == 1:
        print(i)
        break

# =============================

nums = [1, 2, 3, 2, 4, 3, 5, 1]


seen = {}
result = []

for num in nums:
    if num in seen:
        seen[num] += 1
    else:
        seen[num] = 1

for num in nums:
    if seen[num] == 1:
        result.append(num)
print(result) 

# =============================

nums = [1, 3, 2, 3, 4, 3, 2, 1, 1]

seen = {}

max_count = 0

result = []

for n in nums:
    if n in seen:
        seen[n] += 1
    else:
        seen[n] = 1

for c in seen.values():
    if c > max_count:
        max_count = c

for num, c in seen.items():
    if c == max_count:
        result.append(num)
print(result)

# =============================

nums = [5, 7, 5, 7, 5, 8, 8, 7]

seen = {}

for i in nums:
    if i in seen:
        seen[i]+=1
    else:
        seen[i]=1

result = []
max_c = 0

for c in seen.values():
    if c > max_c:
        max_c = c

for num, c in seen.items():
    if c == max_c:
        result.append(num)
print(result)



























