def swap(arr: list, i: int, j: int) -> None:
    arr[i], arr[j] = arr[j], arr[i]


def heapify(arr: list, n: int, i: int) -> None:

    # param end: Index in arr[] to heapify
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # left child index
    right = 2 * i + 2  # right child index

    # If left child is larger than root
    if left < n and arr[largest] < arr[left]:
        largest = left

    # If right child is larger than largest so far
    if right < n and arr[largest] < arr[right]:
        largest = right

    # If largest is not root
    if largest != i:
        swap(arr, i, largest)  # swap

        # Heapify the root.
        heapify(arr, n, largest)


def heap_sort(arr: list) -> list:
    n = len(arr)

    if n <= 1:
        return arr

    for i in range((n - 1) // 2, -1, -1):
        heapify(arr, n, i)

    # extract and push max element to right as sorted part
    # heapify excluding sorted part from i
    for i in range(n - 1, 0, -1):
        swap(arr, i, 0)  # swap
        heapify(arr, i, 0)

    return arr


# Test Cases
if __name__ == "__main__":
    print (heap_sort([12, 11, 13, 5, 6, 7]))

    # Test Case 1: Testing with a list of integers
    assert heap_sort([12, 11, 13, 5, 6, 7]) == [5, 6, 7, 11, 12, 13], "Test Case 1 Failed"

    # Test Case 2: Testing with an already sorted list
    assert heap_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], "Test Case 2 Failed"

    # Test Case 3: Testing with a list containing negative numbers
    assert heap_sort([-3, -1, -2, -4, -5]) == [-5, -4, -3, -2, -1], "Test Case 3 Failed"

    print("All test cases passed!")