n = int(input())
def Nqueens(n):
    ans = []
    grid = [['.']*n for _ in range(n)]
    def valid_queens(row = 0, cols = [], posl = [], negl = []):
        if row == n:
            ans.append([''.join(row) for row in grid])
            return
        for col in range(n):
            if col in cols or (row + col) in posl or (row - col) in negl:
                continue
            grid[row][col] = 'Q'
            valid_queens(row + 1, cols + [col], posl + [row + col], negl + [row - col])
            grid[row][col] = '.'
    valid_queens()
    return ans
ans = Nqueens(n)
for queens in ans:
    print(*queens, sep = '\n')
    print()