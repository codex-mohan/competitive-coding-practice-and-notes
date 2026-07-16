# LeetCode #3532: Path Existence Queries in a Graph
# https://leetcode.com/problems/path-existence-queries-in-a-graph/
#
# Difficulty: Hard
# Tags: Graph, Component Labeling
#
# Approach: Component Labeling via Adjacency
# - Two adjacent indices are connected if |nums[i] - nums[i-1]| <= maxDiff.
# - Assign component IDs: same component if adjacent diff <= maxDiff.
# - A query (u, v) is reachable iff comp[u] == comp[v].
#
# Time:  O(n + q) — one pass to label, one pass to answer queries
# Space: O(n) — component array

from typing import List


class Solution:
    def pathExistenceQueries(
        self,
        n: int,
        nums: List[int],
        maxDiff: int,
        queries: List[List[int]]
    ) -> List[bool]:

        # Step 1: Assign component IDs based on adjacency constraint
        comp = [0] * n
        component_id = 0

        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                component_id += 1       # gap too large -> new component
            comp[i] = component_id

        # Step 2: Answer queries — same component = path exists
        ans = []
        for u, v in queries:
            ans.append(comp[u] == comp[v])

        return ans


# --------------- Tests ---------------
if __name__ == "__main__":
    sol = Solution()

    # Two nodes, connected
    assert sol.pathExistenceQueries(
        n=2, nums=[1, 2], maxDiff=1, queries=[[0, 1]]
    ) == [True]

    # Two nodes, disconnected
    assert sol.pathExistenceQueries(
        n=2, nums=[1, 5], maxDiff=1, queries=[[0, 1]]
    ) == [False]

    # Three nodes: 1-2 connected, 2-3 disconnected
    assert sol.pathExistenceQueries(
        n=3, nums=[1, 2, 10], maxDiff=1, queries=[[0, 1], [0, 2], [1, 2]]
    ) == [True, False, False]

    # All connected
    assert sol.pathExistenceQueries(
        n=4, nums=[1, 2, 3, 4], maxDiff=1, queries=[[0, 3]]
    ) == [True]

    # None connected
    assert sol.pathExistenceQueries(
        n=3, nums=[1, 10, 20], maxDiff=1, queries=[[0, 1], [1, 2]]
    ) == [False, False]

    # Same node query
    assert sol.pathExistenceQueries(
        n=3, nums=[1, 5, 10], maxDiff=1, queries=[[1, 1]]
    ) == [True]

    print("All tests passed!")
