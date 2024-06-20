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
        length -= 1
        substring = substring[1:]
max_len = max(length, max_len)
print(max_len)