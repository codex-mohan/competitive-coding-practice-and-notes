import numpy as np
from string import ascii_lowercase

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        m = n // 2

        a = np.frombuffer(s[:m].encode(), dtype=np.uint8)
        count = np.bincount(a - 97, minlength=26)

        half = ''.join(
            ch * int(k)
            for ch, k in zip(ascii_lowercase, count)
        )

        return half + (s[m] if n & 1 else '') + half[::-1]
