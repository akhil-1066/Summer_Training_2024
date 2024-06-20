s = input()
ans = ''
for i in s:
    if i in 'aeiou':
        ans += i.upper()
    elif i.isupper() and i not in 'AEIOU':
        ans += i.lower()
    else:
        ans += i
print(ans)