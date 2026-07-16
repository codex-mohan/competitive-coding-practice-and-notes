# LeetCode #3867: GCD Sum
# https://leetcode.com/problems/gcd-sum/
#
# Difficulty: Hard
# Tags: GCD, Prefix, Two Pointers, Sorting
#
# Approach:
# - Build prefix GCD array: prefixGCD[i] = gcd(prefixGCD[i-1], nums[i])
#   after taking max so far (prefixMax tracks running max).
# - Sort the prefixGCD array.
# - Use two pointers from both ends, summing gcd(left, right) pairs.
#
# Time:  O(n log n) — sort dominates
# Space: O(n) — prefixGCD array

import math
from typing import List


class Solution:
    def gcdSum(self, nums: List[int]) -> int:
        # Step 1: Build prefix GCD array
        prefixMax = 0
        prefixGCD = []

        for x in nums:
            prefixMax = max(prefixMax, x)
            prefixGCD.append(math.gcd(x, prefixMax))

        # Step 2: Sort and pair from both ends
        prefixGCD.sort()

        left = 0
        right = len(prefixGCD) - 1

        result = 0
        while left < right:
            result += math.gcd(prefixGCD[left], prefixGCD[right])
            left += 1
            right -= 1

        return result


# --------------- Tests ---------------
if __name__ == "__main__":
    sol = Solution()

    # Simple: [4, 6, 8] -> prefixMax=[4,6,8], prefixGCD=[4,6,8]
    # sorted=[4,6,8], pairs: gcd(4,8)=4 -> result=4
    assert sol.gcdSum([4, 6, 8]) == 4

    # Single element: no pairs (left == right immediately)
    assert sol.gcdSum([10]) == 0

    # Two elements
    assert sol.gcdSum([6, 12]) == 6

    # All same
    assert sol.gcdSum([5, 5, 5]) == 5

    # Increasing sequence
    assert sol.gcdSum([1, 2, 3, 4]) > 0

    print("All tests passed!")
