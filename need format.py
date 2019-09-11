import sys


def trans(ch):
    if ord(ch) in range(48, 58):
        return ord(ch) - 48
    else:
        return ord(ch) - 55


def func(s):
    res = list()
    h, m = s.split(':')
    h, m = list(reversed(list(map(trans, h)))), list(reversed(list(map(trans, m))))
    low = max(max(h), max(m))
    for base in range(low + 1, 61):
        sum_h = sum_m = 0
        for idx, num in enumerate(h):
            sum_h += num * (base ** idx)
        for idx, num in enumerate(m):
            sum_m += num * (base ** idx)

        if sum_h < 24 and sum_m < 60:
            res.append(base)

    return res


if __name__ == '__main__':
    s = sys.stdin.readline().strip()
    res = func(s)
    if not res:
        print('-1')
    elif res[-1] == 60:
        print('0')
    else:
        print(' '.join(map(str, res)))
