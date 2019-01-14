def re_match(string, pattern):
    # 几种特殊情况
    if string is None or pattern is None:
        return False
    elif len(string) == 0 and len(pattern) == 0:
        return True
    elif len(string) > 0 and len(pattern) == 0:
        return False

    # 匹配位置后面出现"*"的情况，"*"的优先级要高于"."
    elif len(pattern) > 1 and pattern[1] == '*':
        # 分为两种情况，可以匹配或无法匹配
        if len(string) > 0 and (string[0] == pattern[0] or pattern[0] == '.'):  # 可以匹配，字符相等或出现任意符
            return (re_match(string, pattern[2:]) or  # 跳过'*'
                    re_match(string[1:], pattern[2:]) or  # '*'匹配一次
                    re_match(string[1:], pattern))  # '*'匹配多次
        else:  # 无法匹配
            return re_match(string, pattern[2:])

    # 匹配成功的情况，字符相等或遇到任意匹配符"."
    elif len(string) > 0 and (string[0] == pattern[0] or pattern[0] == '.'):
        return re_match(string[1:], pattern[1:])

    # 字符不等
    else:
        return False
