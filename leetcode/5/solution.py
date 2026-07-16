# LeetCode #5: Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/
#
# Difficulty: Medium
# Tags: Two Pointers, Expand Around Center, String
#
# Approach: Expand Around Center
# - Every palindrome has a center. Try every possible center:
#   - Odd-length:  center is a single character (i, i)
#   - Even-length: center is between two characters (i, i+1)
# - From each center, expand outward while characters match.
# - Track the longest palindrome found.
#
# Time:  O(n^2) — n centers, each expanding up to O(n)
# Space: O(1)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        if n <= 1:
            return s

        start = 0
        max_len = 1

        def expand(left: int, right: int) -> None:
            """Expand outward from center (left, right) and update global best."""
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
            expand(i, i)       # odd length:  "aba"
            expand(i, i + 1)   # even length: "abba"

        return s[start:start + max_len]


# --------------- Tests ---------------
if __name__ == "__main__":
    sol = Solution()

    # Basic cases
    assert sol.longestPalindrome("babad") in ("bab", "aba"), "bab or aba"
    assert sol.longestPalindrome("cbbd") == "bb", "bb"

    # Single char
    assert sol.longestPalindrome("a") == "a"

    # All same
    assert sol.longestPalindrome("aaaa") == "aaaa"

    # Full string is palindrome
    assert sol.longestPalindrome("racecar") == "racecar"

    # Even-length palindrome
    assert sol.longestPalindrome("abba") == "abba"

    # No palindrome longer than 1
    assert sol.longestPalindrome("abcde") in ("a", "b", "c", "d", "e")

    print("All tests passed!")
