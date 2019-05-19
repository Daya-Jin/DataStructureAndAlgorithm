def findLUSlength(strs) -> int:
    strs = list(set(strs))    # 去重优化
    strs.sort(key=len, reverse=True)
    res = -1

    def isSub(s1, s2):
        '''
        判断s1是不是s2的一个子序列，len(s1)<=len(s2)
        '''
        i = 0
        for ch in s2:
            if ch == s1[i]:
                i += 1
                if i == len(s1):
                    return True
        return False

    for i in range(len(strs)):    # 选出的字串
        for j in range(i):    # 比较的字串
            if i != j and isSub(strs[i], strs[j]):
                break
            if j == i-1:
                res = max(res, len(strs[i]))

    return res


findLUSlength(["aabbcc", "aabbcc","bc","bcc","aabbccc"])