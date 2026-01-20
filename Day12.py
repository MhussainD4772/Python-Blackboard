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

s = "aabbbcbcd"

seen = {}

for i in s:
    if i not in seen:
        seen[i] = 1
    else:
        seen[i] += 1
        print(i)
        break

    
        
