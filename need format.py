def nextGreaterElements(nums):
    double_nums = nums+nums
    s = list()
    table = dict()

    for num in nums:
        if not s:
            s.append(num)
            continue

        while s and num > s[-1]:
            pre_num = s.pop()
            table[pre_num] = num

        s.append(num)

    while s:
        pre_num = s.pop()
        if pre_num not in table.keys():
            table[pre_num] = -1

    return [table[num] for num in nums]

nextGreaterElements([3,2,1])