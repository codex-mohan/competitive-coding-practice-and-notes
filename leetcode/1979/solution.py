from math import gcd
from typing import List

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mn, mx = min(nums), max(nums)
        n = len(nums)

        print(mn, mx)

        GCD = 1
        for i in range(1,mn + 1):
            if mx % i == 0 and mn % i == 0:
                GCD = max(GCD, i)
                print(f'GCD at {i}: {GCD}')

        return GCD

if __name__ == '__main__':
    s = Solution()
    res = s.findGCD([2,5,6,9,10])
    print('result', res)
