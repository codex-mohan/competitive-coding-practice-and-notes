# Standard Method Numerical

def BinarySearch(arr: list[int], target):
    low, high = 0, len(arr) - 1

    while low < high:
        mid = (low + high) // 2
        if arr[mid] > target:
            low = mid + 1
        else:
            high = mid - 1
        if arr[mid] == target:
            return mid
    return -1
