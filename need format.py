# 思路：考虑从一个中心字符或两个中心字符往左右扩展
# 如果扩展后的左右两字符相等，则生成新的回文


def longestPalindrome(s: str) -> str:
    res = ''
    if not s:
        return res

    for cent_idx in range(len(s)):
        l, r = cent_idx, cent_idx    # 单个字符的初始边界
        while l >= 0 and r < len(s) and s[l] == s[r]:
            # 扩展
            l -= 1
            r += 1
        if r-l+1 > len(res):
            res = s[l:r+1]

        l, r = cent_idx, cent_idx+1    # 两个字符的初始边界
        while l >= 0 and r < len(s) and s[l] == s[r]:
            # 扩展
            l -= 1
            r += 1
        if r-l+1 > len(res):
            res = s[l:r+1]

    return res


longestPalindrome("cbbd")