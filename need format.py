def computeArea(A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
    ld_1, ru_1, ld_2, ru_2 = (A, B), (C, D), (E, F), (G, H)

    # 求两矩形的面积和
    res = (ru_1[0]-ld_1[0])*(ru_1[1]-ld_1[1])  \
        + (ru_2[0]-ld_2[0])*(ru_2[1]-ld_2[1])

    # 重叠坐标
    ld_overlap = (max(ld_1[0], ld_2[0]), max(ld_1[1], ld_2[1]))
    ru_overlap = (min(ru_1[0], ru_2[0]), min(ru_1[1], ru_2[1]))

    if ld_overlap[0] > ru_overlap[0] and ld_overlap[1] < ru_overlap[1]:
        res -= (ru_overlap[0]-ld_overlap[0])*(ru_overlap[1]-ld_overlap[1])

    return res


computeArea(A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2)