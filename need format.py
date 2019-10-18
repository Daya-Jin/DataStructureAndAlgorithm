import sys


def func(mat, r1, c1, r2, c2, t):
    n, m = len(mat), len(mat[0])
    dp = [[[0] * m for _ in range(n)] for _ in range(t + 1)]
    for z in range(1, t + 1):
        for y in range(n):
            for x in range(m):
                if mat[x][y] == '*':
                    continue
                up = down = left = right = 0
                if y > 0:
                    up = 1 if y == r2 + 1 and x == c2 else dp[z - 1][y - 1][x]
                if y < n - 1:
                    down = 1 if y == r2 - 1 and x == c2 else dp[z - 1][y + 1][x]
                if x > 0:
                    left = 1 if x == c2 + 1 and y == r2 else dp[z - 1][y][x - 1]
                if x < m - 1:
                    right = 1 if x == c2 - 1 and y == r2 else dp[z - 1][y][x + 1]
                dp[z][x][y] = up + down + left + right

    return dp[-1][r1][c1]


n, m, t = list(map(int, sys.stdin.readline().strip().split()))
mat = list()
for _ in range(n):
    mat.append(list(sys.stdin.readline().strip()))

r1, c1, r2, c2 = list(map(int, sys.stdin.readline().split()))
print(func(mat, r1 - 1, c1 - 1, r2 - 1, c2 - 1, t))
