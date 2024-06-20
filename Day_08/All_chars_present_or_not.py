s = input()
for i in range(97,123):
    if chr(i) not in s:
        print('NO')
        break
else:
    print('Yes')