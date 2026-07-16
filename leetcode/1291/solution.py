# LeetCode #1291: Sequential Digits
# https://leetcode.com/problems/sequential-digits/
#
# Difficulty: Medium
# Tags: Enumeration, Math, Brute Force
#
# Approach: Enumerate All Sequential Numbers
# - A sequential-digit number has digits like 123, 234, 3456, etc.
# - There are only 36 such numbers (at most 9+8+...+1 = 45 candidates).
# - For each starting digit (1-9), build numbers by appending the next digit.
# - Collect those falling within [low, high].
#
# Time:  O(1) — bounded by fixed number of candidates
# Space: O(1) — output list only

from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []

        for start in range(1, 10):         # starting digit
            num = start
            next_digit = start + 1

            while next_digit <= 9:
                num = num * 10 + next_digit  # append next sequential digit

                if low <= num <= high:
                    result.append(num)

                next_digit += 1

        return sorted(result)


# --------------- Tests ---------------
if __name__ == "__main__":
    sol = Solution()

    # Basic
    assert sol.sequentialDigits(100, 300) == [123, 234]
    assert sol.sequentialDigits(100, 1000) == [123, 234, 345, 456, 567, 678, 789]

    # Edge: low and high are sequential themselves
    assert sol.sequentialDigits(123, 123) == [123]
    assert sol.sequentialDigits(12, 12) == [12]

    # No results in range
    assert sol.sequentialDigits(1000, 1050) == []

    # Large range covers all
    assert sol.sequentialDigits(1, 123456789) == [
        12, 23, 34, 45, 56, 67, 78, 89,
        123, 234, 345, 456, 567, 678, 789,
        1234, 2345, 3456, 4567, 5678, 6789,
        12345, 23456, 34567, 45678, 56789,
        123456, 234567, 345678, 456789,
        1234567, 2345678, 3456789,
        12345678, 23456789,
        123456789,
    ]

    print("All tests passed!")
