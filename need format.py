# 思路：设置新数组，原数组设双指针，逐位比较元素并插入新数组

def merge(nums1, m, nums2, n):
    if not nums1:
        return nums2
    if not nums2:
        return nums1

    tmp_arr = [None] * (len(nums1) + len(nums2))
    idx1 = idx2 = idx_tmp = 0

    while idx1 < len(nums1) and idx2 < len(nums2):
        if nums1[idx1] < nums2[idx2]:
            tmp_arr[idx_tmp] = nums1[idx1]
            idx1 += 1
        else:
            tmp_arr[idx_tmp] = nums2[idx2]
            idx2 += 1
        idx_tmp += 1

    if idx1 == len(nums1) - 1:
        tmp_arr[idx_tmp:] = nums2[idx2:]
    if idx2 == len(nums2) - 1:
        tmp_arr[idx_tmp:] = nums1[idx1:]

    return tmp_arr


merge([1, 2, 3], 3, [2, 5, 6], 3)