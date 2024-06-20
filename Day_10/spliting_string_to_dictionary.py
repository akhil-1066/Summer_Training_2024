s = input()
d = {key: val for key, val in [data.split(':') for data in s.split(',')]}
#print(d)
ans = ''
for key in d:
    l = len(key)
    for num in range(l,0,-1):
        if str(num) in d[key]:
            ans += key[num-1]
            break
    else:
        ans += 'x'
print(ans)

# Input: hello:5438,car:214,book:8799,apple:2187
# Output: oaxp