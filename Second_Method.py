s = 'ABCDEFGEFAEFG'
sb = 'EFG'
results = 0
sub_len = len(sb)
for i in range(len(s)):
    if s[i:i+sub_len] == sb:
        results += 1

print("Occurrence of sub string: ",results)


