# 思路：典型的栈应用

def evalRPN(tokens):
    s = list()

    opt = set(['+', '-', '*', '/'])

    for ch in tokens:
        if ch in opt:
            op2 = s.pop()
            op1 = s.pop()
            if ch == '+':
                s.append(op1 + op2)
            elif ch == '-':
                s.append(op1 - op2)
            elif ch == '*':
                s.append(op1 * op2)
            elif ch == '/':
                if op2 == 0:
                    s.append(0)
                else:
                    s.append(op1 // op2)
        else:
            s.append(int(ch))

    return s[-1]


evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])