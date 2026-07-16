# Two types of 2-pointer
# # 1) Uni-directional
# # 2) Bidirectional (two pointers move in opposite to each other)

# Bi-directional Example 1: Find the 2 elements in the array which will target to the sum (finds only one result)

def sumToTarget(arr: list[int], target: int) -> list[int]:
    left = 0
    right = len(arr) - 1

    result = 0

    while left < right:
        sum = arr[left] + arr[right]
        if sum > target:
            right -= 1
        elif sum < target:
            left += 1
        else:
            break
    return [left,right]

# Bi-directional 2 - same as ex 1 but includes all pair of number that sum to target
def sumToTargetAllCombinations(arr: list[int], target: int) -> list[list[int]]:
    left, right, results = 0, len(arr) - 1, []

    while left < right:
        total = arr[left] + arr[right]
        if total > target:
            right -= 1
        elif total < target:
            left += 1
        else:
            results.append([left,right])
            left += 1
            right -= 1
    return results


arr = [1,2,3,4,5]
target = 6

res_single = sumToTarget(arr, target)
res_multi = sumToTargetAllCombinations(arr, target)

print(f'result for single pair:{res_single}')
print(f'result for multiple paris:{res_multi}')
