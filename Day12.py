s = "mississippi"

seen = {}
result = []
for ch in s:
    if ch in seen:
        seen[ch] += 1
    else:
        seen[ch] = 1
for ch in s:
    if seen[ch] > 1 and ch not in result:
        result.append(ch)

#=======================================>

s = "abcaabcd"


        
