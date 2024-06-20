password = input()
n = len(password)
u = l = s = d = 0
for char in password:
    if char.isupper():
        u = 1
    elif char.islower():
        l = 1
    elif char.isdigit():
        d = 1
    else:
        s = 1
valid  = l + u + d + s
ans = max(8-n, 4-valid)
if not ans:
    print(-1)
else:
    print(ans)