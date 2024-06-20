n = int(input())
grid = [list(map(int,input().split())) for _ in range(n)]
def Traverse(i,j):
    if (not (0<=i<n and 0<=j<n)) or grid[i][j] == 0:
        return
    grid[i][j] = 0
    Traverse(i, j+1)
    Traverse(i, j-1)
    Traverse(i+1, j)
    Traverse(i-1, j)
i, j = map(int,input().split())
Traverse(i-1,j-1)
print(sum([sum(row) for row in grid]))