n = int(input())
for i in range(n):
    print('_'*(n-i),end = '')
    print('* '*(i),end = '')
    print('*'+'_'*(n-i))