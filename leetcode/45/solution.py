# LeetCode #45: Jump Game II
# https://leetcode.com/problems/jump-game-ii/
#
# Difficulty: Medium
# Tags: Greedy, BFS, Array
#
# Approach: Greedy Range Expansion
# - Track the farthest index reachable within the current jump range.
# - When we exhaust the current range, we must jump (increment count)
#   and extend the range to the farthest point we found.
# - This guarantees minimum jumps because we always choose the
#   jump that reaches the farthest within the current window.
#
# Time:  O(n) — single pass through the array
# Space: O(1) — only a few variables

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        jumps = 0
        current_end = 0   # farthest index reachable with current jumps
        farthest = 0      # farthest index reachable from any index in current range

        for i in range(n - 1):  # no need to jump from last index
            # Update the farthest we can reach from index i
            farthest = max(farthest, i + nums[i])

            # If we've reached the end of the current range, we must jump
            if i == current_end:
                jumps += 1
                current_end = farthest

                # Early exit: if we can already reach the end
                if current_end >= n - 1:
                    break

        return jumps


# --------------- Tests ---------------
if __name__ == "__main__":
    sol = Solution()

    # Basic: 2 jumps needed (0->1->3 or 0->2->3)
    assert sol.jump([2, 3, 1, 1, 4]) == 2

    # Single element: already at end
    assert sol.jump([0]) == 0

    # Two elements: 0 jumps if already at end, 1 if not
    assert sol.jump([1, 0]) == 1

    # All ones: each jump goes exactly 1 step
    assert sol.jump([1, 1, 1, 1]) == 3

    # Large jumps: can reach end in 1 jump
    assert sol.jump([10, 0, 0, 0, 0]) == 1

    # Mixed: 2 jumps
    assert sol.jump([2, 1, 3, 1, 1, 1]) == 2

    # Greedy choice matters: jump to index with best future reach
    assert sol.jump([1, 2, 1, 1, 1]) == 3

    # Edge: minimum jumps = n-1 (each jump goes 1 step)
    assert sol.jump([1, 1, 1, 1, 1]) == 4

    print("All tests passed!")
