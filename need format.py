# 思路：俯视图的面积最容易，为立方柱的个数，即求矩阵中非零元素的个数
# 两个侧视图，分别对应矩阵每行最大值的和与每列最大值的和

def projectionArea(grid) -> int:
    if not grid:
        return None

    n = len(grid)

    area = 0
    for row in range(n):
        row_max, col_max = 0, 0
        for col in range(n):
            if grid[row][col]:
                area += 1

            row_max = max(row_max, grid[row][col])

            # 由于是立方矩阵，在行扫描的同时，交换行列坐标即可实现列扫描
            row_col = max(col_max, grid[col][row])

        area += row_max
        area += col_max

    return area


projectionArea([[1, 2],
                [3, 4]])