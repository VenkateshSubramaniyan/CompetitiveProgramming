def converttoBinary(num: int):
    res = 0
    while num > 0:
        res = res * 10 + (num % 2)
        num //= 2
    return res


def convertToDeicmal(num: int):
    res = 0
    i = 0
    while not num // 10 == 0:
        res += 1 << i
        num = num // 10
        i += 1
    return res


print(converttoBinary(5))
print(convertToDeicmal(100))
