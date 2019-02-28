# 思路：空间换时间，建立两个ASCII码表，key为ASCII码，val为出现位置

def isIsomorphic(s, t):
    if len(s) != len(t):
        return False

    table_s, table_t = [0] * 256, [0] * 256
    for idx in range(len(s)):
        if table_s[ord(s[idx])] != table_t[ord(t[idx])]:
            return False
        table_s[ord(s[idx])] = idx + 1  # 出现位置
        table_t[ord(t[idx])] = idx + 1

    return True


isIsomorphic('ab', 'aa')