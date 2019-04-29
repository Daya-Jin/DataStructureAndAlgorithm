def solve(board) -> None:
    if not board or not board[0]:
        return board
    rows, cols = len(board), len(board[0])

    def trans_rec(row, col):
        if board[row][col] == 'O':
            board[row][col] = '#'
            if row > 0 and board[row-1][col] == 'O':
                trans_rec(row-1, col)
            if row < cols-1 and board[row+1][col] == 'O':
                trans_rec(row+1, col)
            if col > 0 and board[row][col-1] == 'O':
                trans_rec(row, col-1)
            if col < cols-1 and board[row][col+1] == 'O':
                trans_rec(row, col+1)

    # 将跟边缘连接的'O'保护起来
    for row in range(rows):
        for col in range(cols):
            if (board[row][col] == 'O' and (row == 0 or col == 0 or row == rows-1 or col == cols-1)):
                trans_rec(row, col)

    print(board)

    for row in range(rows):
        for col in range(cols):
            if board[row][col] == 'O':
                board[row][col] = 'X'
            if board[row][col] == '#':
                board[row][col] = 'O'


mat = [["X", "O", "X", "O", "X", "O"],
       ["O", "X", "O", "X", "O", "X"],
       ["X", "O", "X", "O", "X", "O"],
       ["O", "X", "O", "X", "O", "X"]]
solve(mat)
mat