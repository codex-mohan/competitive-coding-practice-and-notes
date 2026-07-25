class Solution:
    def maxProduct(self, n: int) -> int:
        nums = str(n)
        lst = [int(s) for s in nums]
        lst.sort(reverse=True)

        return lst[0] * lst[1]
