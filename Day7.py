#You are given a list of payment events, where each event contains a `payment_id`, `amount`, and `timestamp`, and the events may include duplicates because the same payment can be sent multiple times; write a function that processes the events in arrival order and returns a list containing only the first occurrence of each `payment_id`, ignoring all subsequent duplicates while preserving the original order of valid payments.

# from typing import List, Tuple

# def duplicate_payment(events):

#     seen_payment_ids = set()
#     result = []

#     for payment_id, amount, timestamp in events:
#         if payment_id not in seen_payment_ids:
#             seen_payment_ids.add(payment_id)
#             result.append((payment_id,amount,timestamp))
#     return result


# events = [
#     ("p1", 100, 1),
#     ("p2", 200, 2),
#     ("p1", 100, 3),
#     ("p3", 300, 4),
#     ("p2", 200, 5)
# ]

# print(duplicate_payment(events))



# =============================



    


