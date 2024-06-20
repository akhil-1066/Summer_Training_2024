l = list(map(float,input().split()))
f = o = e = 0
for i in l:
    if not (i*10)%10:#  i.is_integer()
        if int(i) & 1:
            o += int(i)
        else:
            e += int(i)
    else:
        f += i
print(o,e,f)