# 思路：程序实现时是逐行逐列扫描并改变矩阵值的，那么怎么保存转换之前的转态是关键
# 使用状态码，不难得出有四种可能的状态：
# 0.死细胞变死细胞；1.活细胞变死细胞；2.死细胞变活细胞；3.活细胞变活细胞
# 注意这里状态码的设置有一个技巧，状态码模2为转换前的存活状态，状态码整除2为转换后的存活状态
# 并且模2运算的状态与初始状态相同
# 扫描矩阵两次，第一次做模运算设置状态码，第二次做整除运算设置存活状态


# def gameOfLife(board) -> None:
def gameOfLife(board) -> None:
    rows, cols = len(board), len(board[0])
    delta = zip([-1, -1, -1, 0, 1, 1, 1, 0], [-1, 0, 1, 1, 1, 0, -1, -1])

    def check_staus(row, col):
        live_nb = 0  # 转换前存活的邻居数

        for dx, dy in delta:
            x = row + dx
            y = col + dy
            if 0 <= x < rows and 0 <= y < cols and board[x][y] % 2 == 1:
                live_nb += 1

        if board[row][col] % 2 == 0 and live_nb == 3:  # 死细胞复活
            return 2
        elif board[row][col] % 2 == 1:  # 之前为活细胞
            if live_nb == 2 or live_nb == 3:  # 存活
                return 3
            else:  # 死亡
                return 1
        else:
            return 0

    # 设置状态码
    for row in range(rows):
        for col in range(cols):
            board[row][col] = check_staus(row, col)

    for row in range(rows):
        for col in range(cols):
            board[row][col] = board[row][col] // 2

    return board


gameOfLife([
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1],
    [0, 0, 0]
])