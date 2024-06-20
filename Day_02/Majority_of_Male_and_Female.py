s = input()
count = 0
for char in s:
    if char == 'M':
        count += 1
    else:
        count -= 1
if count<0:
    print('F')
elif count>0:
    print('M')
else:
    print(0)