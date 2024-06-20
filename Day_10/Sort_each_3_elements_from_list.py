l = list(map(int,input().split()))
for i in range(len(l)-2):
    s = l[i] + l[i+1] + l[i+2]
    l[i], l[i+2] = min(l[i], l[i+1], l[i+2]), max(l[i], l[i+1], l[i+2])
    l[i+1] = s - l[i] - l[i+2]
print(l)

# Input: 4 9 8 2 14 3 5 6
# Output: [4, 2, 8, 3, 5, 6, 9, 14]