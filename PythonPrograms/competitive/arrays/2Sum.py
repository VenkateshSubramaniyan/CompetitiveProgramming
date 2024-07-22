def hi() -> []:
    numbers = [2, 7, 11, 15]
    target = 9
    leftPtr, RightPtr = 0, len(numbers) - 1
    while leftPtr < RightPtr:
        if numbers[leftPtr] + numbers[RightPtr] == target:
            return [leftPtr, RightPtr]

        if (numbers[leftPtr] + numbers[RightPtr] < target):
            leftPtr += 1
        if (numbers[leftPtr] + numbers[RightPtr] > target):
            RightPtr -= 1

    return [-1, -1]


print(hi())
