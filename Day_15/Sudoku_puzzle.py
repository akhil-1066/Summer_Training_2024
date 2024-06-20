board = [[5, 3, '.', '.', 7, '.', '.', '.', '.'], [6, '.', '.', 1, 9, 5, '.', '.', '.'], ['.', 9, 8, '.', '.', '.', '.', 6, '.'], [8, '.', '.', '.', 6, '.', '.', '.', 3], [4, '.', '.', 8, '.', 3, '.', '.', 1], [7, '.', '.', '.', 2, '.', '.', '.', 6], ['.', 6, '.', '.', '.', '.', 2, 8, '.'], ['.', '.', '.', 4, 1, 9, '.', '.', 5], ['.', '.', '.', '.', 8, '.', '.', 7, 9]]
for row in board:
    print(*row)
print()
def is_box_valid(x, y, num):
    if num in board[x]:
        return False
    for i in range(9):
        if num == board[i][y]:
            return False
    x = (x//3)*3
    y = (y//3)*3
    for i in range(x, x+3):
        for j in range(y, y+3):
            if board[i][j] == num:
                return False
    return True
def sudoku(i = 0, j = 0):
    if i == 9:
        return True
    if j == 9:
        return sudoku(i + 1)
    if board[i][j] != '.':
        return sudoku(i, j + 1)
    for num in range(1, 10):
        if is_box_valid(i, j, num):
            board[i][j] = num
            if sudoku(i, j + 1):
                return True
            board[i][j] = '.'
sudoku()
for row in board:
    print(*row)