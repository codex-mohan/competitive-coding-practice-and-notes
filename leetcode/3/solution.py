# LeetCode #3: Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
#
# Difficulty: Medium
# Tags: Sliding Window, Hash Map, String
#
# Approach: Sliding Window with Last-Seen Index Map
# - Maintain a window [left..right] with no repeating characters.
# - Track the last index where each character was seen.
# - When a重复 is found inside the window, jump left past the previous occurrence.
# - Update max length at every step.
#
# Time:  O(n)
# Space: O(min(n, alphabet_size))

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}       # char -> last index
        left = 0
        max_len = 0

        for right, ch in enumerate(s):
            # If ch was seen inside the current window, shrink from the left
            if ch in last_seen and last_seen[ch] >= left:
                left = last_seen[ch] + 1

            last_seen[ch] = right
            max_len = max(max_len, right - left + 1)

        return max_len


# --------------- Tests ---------------
if __name__ == "__main__":
    sol = Solution()

    # Basic cases
    assert sol.lengthOfLongestSubstring("abcabcbb") == 3, "abc"
    assert sol.lengthOfLongestSubstring("bbbbb")    == 1, "b"
    assert sol.lengthOfLongestSubstring("pwwkew")   == 3, "wke"

    # Edge cases
    assert sol.lengthOfLongestSubstring("")   == 0, "empty"
    assert sol.lengthOfLongestSubstring("a")  == 1, "single"
    assert sol.lengthOfLongestSubstring("ab") == 2, "all unique"

    # Longer string
    assert sol.lengthOfLongestSubstring("dvdf") == 3, "vdf"

    print("All tests passed!")
