n = int(input())
island = [list(map(int,input().split())) for _ in range(n)]
def is_island(i, j):
    if not (0 <= i < n and 0 <= j < n) or (not island[i][j]):
        return 0
    island[i][j] = 0
    return 1 + is_island(i + 1, j) + is_island(i - 1, j) + is_island(i, j + 1) + is_island(i, j - 1)
count = 0
max_area = 0
for i in range(n):
    for j in range(n):
        if island[i][j]:
            max_area = max(max_area, is_island(i, j))
            count += 1
print('No. of Island: ', count)
print('Max_area of Islands:', max_area)