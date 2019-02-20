# 思路：归并排序

def InversePairs(numbers):
    if not numbers:
        return 0

    copy_num = numbers[:]
    cnt = InversePairsRec(numbers, copy_num, 0, len(numbers) - 1)  # 递归归并排序并计数
    return cnt


def InversePairsRec(numbers, copy_num, start, end):
    if start == end:  # 单元素
        copy_num[start] = numbers[start]
        return 0

    mid = (end + start) // 2

    # 将左右两部分递归排序并计数
    left_cnt = InversePairsRec(numbers, copy_num, start, mid)
    right_cnt = InversePairsRec(numbers, copy_num, mid + 1, end)

    # 在左右部分均有序之后，对该轮排序并计数。从最大(右)的元素开始往前计数
    left_idx = mid
    right_idx = end
    copy_idx = end
    cnt = 0
    # 左右部分均从后往前排序
    while left_idx >= start and right_idx > mid:
        if numbers[left_idx] > numbers[right_idx]:  # 如果左边值最大值大于右边最大值
            copy_num[copy_idx] = numbers[left_idx]  # 在copy_num中放置最大值再移动指针
            copy_idx -= 1
            left_idx -= 1
            cnt += right_idx - mid  # 左边最大值肯定大于右边所有值，逆序对=右边值的数
        else:  # 若右边最大值已经有序
            copy_num[copy_idx] = numbers[right_idx]  # 则直接放置，再移动指针
            copy_idx -= 1
            right_idx -= 1
    # 将numbers的剩余部分放入copy_num
    while left_idx >= start:
        copy_num[copy_idx] = numbers[left_idx]
        copy_idx -= 1
        left_idx -= 1
    while right_idx > mid:
        copy_num[copy_idx] = numbers[right_idx]
        copy_idx -= 1
        right_idx -= 1

    return cnt + left_cnt + right_cnt


InversePairs([1, 2, 1, 2, 1])