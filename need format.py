# 思路：使用双指针往中心遍历即可
# 假定字符串中还包含复杂字符，需要过滤

def isPalindrome(s):
    if len(s) < 2:
        return True

    l_idx, r_idx = 0, len(s) - 1
    while l_idx < r_idx:
        while not s[l_idx].isalnum and l_idx < r_idx:
            l_idx += 1
        while not s[r_idx].isalnum and l_idx < r_idx:
            r_idx -= 1

        if s[l_idx].lower() != s[r_idx].lower():
            return False

        l_idx += 1
        r_idx -= 1

    return True


isPalindrome("A man, a plan, a canal: Panama")