s = input()
count = 1
i, n= 1, len(s)
while i<n:
    if s[i] == s[i-1]:
        count += 1
    else:
        print(s[i-1]+str(count),end = '')
        count = 1
    i+=1
print(s[-1]+str(count))