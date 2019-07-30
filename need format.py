def myPow(x: float, n: int) -> float:
    if n < 0:
        return myPow(x, abs(n))

    if n == 0:
        return 1

    if n & 1 == 0:
        return myPow(myPow(x, n >> 1), 2)
    else:
        return myPow(myPow(x, n >> 1), 2) * x


myPow(2, 2)