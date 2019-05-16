def convert(s: str, numRows: int) -> str:
    if numRows < 2 or len(s) < 2:
        return s

    res = list()
    len_clc = 2 * numRows - 2  # 周期长度
    len_s = len(s)

    for row in range(numRows):
        idx = row
        while idx < len_s:
            res.append(s[idx])
            if row != 0 and row != numRows - 1:
                ex_idx = idx + len_clc - 2 * row
                if ex_idx < len_s:
                    res.append(s[ex_idx])
            idx += len_clc

    return ''.join(res)


convert('PINALSIGYAHRPI', 4)