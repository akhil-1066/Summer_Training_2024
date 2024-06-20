l = list(map(int,input().split()))
for i in range(len(l)-2):
    for j in range(i+1,len(l)-1):
        for k in range(j+1, len(l)):
            print((l[i], l[j], l[k]))