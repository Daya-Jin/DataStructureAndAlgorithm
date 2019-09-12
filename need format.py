import sys


def func(x_u, y_u, xs, ys):
    res = False
    n = len(xs)
    i, j = 0, n - 1
    while i < n:
        if ((ys[i] > y_u) != (ys[j] > y_u)
                and (x_u < (xs[j] - xs[i]) * (y_u - ys[i]) / (ys[j] - ys[i]) + xs[i])):
            res = not res
        j = i
        i += 1

    return res


coord = sys.stdin.readline().strip().split()
x_u, y_u = list(map(float, coord[0].split(',')))
xs = list(map(float, [item.split(',')[0] for item in coord[1:]]))
ys = list(map(float, [item.split(',')[1] for item in coord[1:]]))

print(xs, ys, x_u, y_u)
print(func(x_u, y_u, xs, ys))
