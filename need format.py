def canPlaceFlowers(flowerbed, n: int) -> bool:
    cnt = 0

    for i in range(len(flowerbed)):
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == n - 1 or flowerbed[i + 1] == 0):
            flowerbed[i] = 1
            cnt += 1

            if cnt >= n:
                return True

    return False


canPlaceFlowers([1, 0, 0, 0, 1, 0, 0], n=2)