class Solution:
    @classmethod
    def uniqueXorTriplets(self, nums: list[int]) -> int:
        n = len(nums)

        if n <= 2:
            return n

        bitLen = n.bit_length()
        maxPossible = 1 << bitLen

        pairs = set()

        for i in range(n + 1):
            for j in range(i,n):
                print(f'index: {i},{j}')
                res = nums[i] ^ nums[j-1] ^ nums[j]
                pairs.add(res)

        print(pairs)

        return len(pairs)

if __name__ == '__main__':
    print(Solution.uniqueXorTriplets([1,3]))
    print(Solution.uniqueXorTriplets([6,7,8,9]))
