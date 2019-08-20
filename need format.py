import sys


def handle_inputs():
    h, w = list(map(int, sys.stdin.readline().split()))
    img = [[0] * w for _ in range(h)]
    for row in range(h):
        cur_row = list(map(int, sys.stdin.readline().split()))
        img[row] = cur_row

    k_size = int(sys.stdin.readline().strip())
    kernel = [[0] * k_size for _ in range(k_size)]
    for row in range(k_size):
        cur_row = list(map(float, sys.stdin.readline().split()))
        kernel[row] = cur_row

    return img, kernel


def conv_opt(row, col, img, kernel, k_size):
    res = 0
    for i in range(k_size):
        for j in range(k_size):
            res += img[row + i][col + j] * kernel[i][j]

    return min(int(res), 255)


def mat2str(mat):
    return '\n'.join(list(map(lambda x: ' '.join(list(map(str,x))), mat)))


if __name__ == '__main__':
    img, kernel = handle_inputs()
    h, w = len(img), len(img[0])
    k_size = len(kernel)

    rows, cols = h - k_size + 1, w - k_size + 1
    res = [[0] * cols for _ in range(rows)]
    for row in range(rows):
        for col in range(cols):
            res[row][col] = conv_opt(row, col, img, kernel, k_size)

    print(mat2str(res))
