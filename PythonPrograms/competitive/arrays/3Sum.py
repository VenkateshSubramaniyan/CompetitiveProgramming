from collections import defaultdict


def hi() -> []:
    nums = [-1, 0, 1, 2, -1, -4]
    negative = defaultdict(int)
    positive = defaultdict(int)
    zeros = 0
    for num in nums:
        if num < 0:
            negative[num] += 1
        elif num > 0:
            positive[num] += 1
        else:
            zeros += 1

    result = []
    if zeros:
        for n in negative:
            if -n in positive:
                result.append((0, n, -n))
        if zeros > 2:
            result.append((0, 0, 0))
    print("single : ")

    negative[-5] = 1
    positive[5] = 1

    for val in negative:
        print(val, end=" ")
    print("\nDouble : ")

    for val1, val2, val3 in (negative, negative):
        print("val1 = {},  val2 = {}".format(val1, val3))
    print("\n")

    for set1, set2 in ((negative, positive), (positive, negative)):
        set1Items = list(set1.items())
        for i, (j, k) in enumerate(set1Items):
            for j2, k2 in set1Items[i:]:
                if j != j2 or (j == j2 and k > 1):
                    if -j - j2 in set2:
                        result.append((j, j2, -j - j2))
    return result


rews = hi()
print(rews)
