class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ones = s.count("1")

        previous_zeros = None
        max_gain = 0
        i = 0
        n = len(s)

        while i < n:
            if s[i] == "1":
                i += 1
                continue

            j = i
            while j < n and s[j] == "0":
                j += 1

            current_zeros = j - i

            if previous_zeros is not None:
                max_gain = max(
                    max_gain,
                    previous_zeros + current_zeros
                )

            previous_zeros = current_zeros
            i = j

        return ones + max_gain
