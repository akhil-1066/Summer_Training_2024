s1 = input()
s2 = input()
s = set()
for char in (s1 + s2):
    if char.isdigit():
        s.add(char)
res = sorted(list(s), reverse = True)
for i in range(len(res) - 1, -1, -1):
    if not int(res[i]) & 1:
        res.append(res.pop(i))
        print('Largest Even Number:', int(''.join(res)))
        break
else:
    print('Largest Even Number is not Possible')