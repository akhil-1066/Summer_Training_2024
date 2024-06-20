n = int(input())
n = 2*n
for i in range(1,n):
    for j in range(1, n):
        print(min(n - i, n - j, i, j), end = ' ')
    print()