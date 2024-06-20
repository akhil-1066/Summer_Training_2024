s = input()
substring = ''
length = max_len = i = 0
while i<len(s):
    if s[i] not in substring:
        substring += s[i]
        length += 1
        i += 1
    else:
        max_len = max(length, max_len)
        ind = substring.index(s[i]) + 1
        length -= ind
        substring = substring[ind:]
max_len = max(length, max_len)
print(max_len)
