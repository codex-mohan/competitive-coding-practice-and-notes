class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n
        k %= total

        flat = [value for row in grid for value in row]
        shifted = flat[-k:] + flat[:-k] if k else flat

        return [
            shifted[i:i + n]
            for i in range(0, total, n)
        ]
