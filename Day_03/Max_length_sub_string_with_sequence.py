s = input()
length = max_length = 1
for i in range(1,len(s)):
    if ord(s[i-1])+1 == ord(s[i]):
        length += 1
    else:
        max_length = max(max_length, length)
        length = 1
max_length = max(max_length, length)        
print(max_length)