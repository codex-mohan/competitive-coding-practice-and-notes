class Solution:
    @classmethod
    def uniqueXorTriplets(self, nums: list[int]) -> int:
        n = len(nums)

        if n <= 2:
            return n

        bitLen = n.bit_length()

        return 1 << bitLen

if __name__ == '__main__':
    print(Solution.uniqueXorTriplets([1,3]))
    print(Solution.uniqueXorTriplets([6,7,8,9]))
