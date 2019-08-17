def func(arr, key):
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) >> 1
        if arr[mid] > arr[left]:  # 左边有序
            if arr[left] <= key <=arr[mid]:
                right = mid
            else:
                left = mid+1
        else:  # 右边有序
            if arr[mid] < key <= arr[right]:
                left=mid+1
            else:
                right = mid

    return left


import sys

arr = list(map(int, sys.stdin.readline().split()))
key = int(sys.stdin.readline().strip())

print(func(arr, key))
