n = int(input())
not_place = tuple(map(int,input().split()))
def Nqueen(n):
    negl = []
    posl = []
    cols = []
    grid = [['.']*n for _ in range(n)]
    ans = []
    def is_valid(row = 0, posl = [], negl = [], cols = []):
        if row == n:
            ans.append([''.join(row) for row in grid])
            return
        for col in range(n):
            if col in cols or (row + col) in posl or (row - col) in negl or (row, col) == not_place:
                continue
            grid[row][col] = 'Q'
            is_valid(row + 1, posl + [row + col], negl + [row - col], cols + [col])
            grid[row][col] = '.'
    is_valid()
    return ans
for nqueen in Nqueen(n):
    print(*nqueen, sep = '\n')
    print()