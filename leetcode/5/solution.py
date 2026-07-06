class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        if n <= 1:
            return s

        start = 0
        max_len = 1

        def expand(left: int, right: int) -> None:
            nonlocal start, max_len

            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1

            # After loop breaks, valid palindrome is from left + 1 to right - 1
            curr_len = right - left - 1

            if curr_len > max_len:
                max_len = curr_len
                start = left + 1

        for i in range(n):
            expand(i, i)       # odd length
            expand(i, i + 1)   # even length

        return s[start:start + max_len]
