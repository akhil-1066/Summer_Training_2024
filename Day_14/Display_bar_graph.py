l = list(map(int,input().split()))
maxx = max(l)
print()
while maxx:
    print(maxx, '|', end = ' ')
    for num in l:
        if num >= maxx:
            print('*', end = ' ')
        else:
            print(' ', end = ' ')
    print()
    maxx -= 1
print('   '+'-'*2*len(l))
print(' '*3, end = ' ')
print(*l, sep = ' ')

'''
Input: 6 3 7 8 2
Output:

8 |       *   
7 |     * *   
6 | *   * *   
5 | *   * *   
4 | *   * *   
3 | * * * *   
2 | * * * * * 
1 | * * * * * 
   ----------
    6 3 7 8 2
'''