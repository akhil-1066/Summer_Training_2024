n, m = map(int, input().split())
obstacle = tuple(map(int, input().split()))
paths = []
def Traverse(i = 0, j = 0, visited = []):
    if (i, j) == (n - 1, m - 1):
        paths.append(visited + [(i, j)])
        return 1
    if not (0<=i<n and 0<=j<m) or (i, j) in visited or (i, j) == obstacle:
        return 0
    return Traverse(i + 1, j, visited + [(i, j)]) + Traverse(i - 1, j, visited + [(i, j)]) + Traverse(i, j + 1, visited + [(i, j)]) + Traverse(i, j - 1, visited + [(i, j)])
print(Traverse())
for path in paths:
    print(*path, sep = '-> ')