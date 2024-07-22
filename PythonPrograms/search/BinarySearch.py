def search(nums: [int], target: int):
    res = binarySearch(nums, 0, len(nums) - 1, target)
    return res


def binarySearch(nums: [int], left: int, right: int, target: int):
    if left <= right:
        mid = int(right + left) // 2
        if (target == nums[mid]):
            return mid
        if (target < nums[mid]):
            return binarySearch(nums, left, mid - 1, target)
        else:
            return binarySearch(nums, mid + 1, right, target)
    return -1


def iterativeBinarySearch(nums: [int], left: int, right: int, target: int):
    while left <= right:
        mid = int(left + right) // 2
        if (nums[mid] == target):
            return mid
        elif (nums[mid] > target):
            right = mid - 1
        else:
            left = mid + 1
    return -1


arr = [1, 3, 7, 9, 11, 12, 45]
# print (search(arr,12))
print(search([-1, 0, 3, 5, 9, 12], 2))
# print (search(arr,120))
