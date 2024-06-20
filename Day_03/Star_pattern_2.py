n = int(input())
for i in range(n):
    s = ''
    for j in range(i+1):
        s += chr(97+j)
    s = s + s[::-1][1:]
    print('-'*(n-i) + s + '-'*(n-i))