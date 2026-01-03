# You are given a list of payment events, where each event contains a `payment_id`, `amount`, and `timestamp`, and the events may include duplicates because the same payment can be sent multiple times; write a function that processes the events in arrival order and returns a list containing only the first occurrence of each `payment_id`, ignoring all subsequent duplicates while preserving the original order of valid payments.

from typing import List, Tuple

def duplicate_payment(events):

    seen_payment_ids = set()
    result = []

    for payment_id, amount, timestamp in events:
        if payment_id not in seen_payment_ids:
            seen_payment_ids.add(payment_id)
            result.append((payment_id,amount,timestamp))
    return result


events = [
    ("p1", 100, 1),
    ("p2", 200, 2),
    ("p1", 100, 3),
    ("p3", 300, 4),
    ("p2", 200, 5)
]

print(duplicate_payment(events))



# =============================

nums = [2, 5, 8, 3, 6]

counter = 0

for n in nums:
    if n % 2 == 0:
        counter += 1
print(counter)


# =============================

nums = [1, 4, 7, 10]

total = 0

for n in nums:
    total += n
print(total)


#  =============================   

nums = [3, 9, 2, 7, 5]

maximum = nums[0]

for n in nums:
    if n > maximum:
        maxium = n
print(maximum)

#  =============================  

nums = [4, 11, 6, 9, 2, 15]

count = 0

for n in nums:
    if n > 5:
        count+=1
print(count)

# =============================  



nums = [3, 12, 7, 20, 5, 18, 1]

even_sum = 0
odd_sum = 0

for n in nums:
    if n % 2 == 0:
        even_sum += n
    else:
        odd_sum += n

print(even_sum)
print(odd_sum)