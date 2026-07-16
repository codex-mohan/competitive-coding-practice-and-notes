---
title: Sliding Window Tricks
---

# Sliding Window Tricks

## 1. The Core Template

Almost every sliding window problem fits this skeleton:

```python
def sliding_window(arr, ...):
    left = 0
    # window state (sum, count, frequency map, etc.)
    result = 0  # or float('inf'), depending on min/max

    for right in range(len(arr)):
        # 1. EXPAND: add arr[right] to window state

        # 2. SHRINK: while window is invalid, move left forward
        while window_is_invalid:
            # remove arr[left] from window state
            left += 1

        # 3. UPDATE: record answer from current valid window
        result = max(result, right - left + 1)  # or similar

    return result
```

**Key insight:** `right` always moves forward (O(n)). `left` only moves forward inside the `while` (amortized O(n)). Total: **O(n)**.

---

## 2. Fixed-Size Window

Window size `k` is known upfront. No `while` shrink — just slide.

```python
# Max sum of any subarray of size k
def max_sum_k(arr, k):
    window_sum = sum(arr[:k])
    best = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]   # slide: add right, drop left
        best = max(best, window_sum)

    return best
```

### Trick: Running Sum Slides

```python
window_sum += arr[right] - arr[right - k]
```

This is O(1) per step — avoid recalculating the sum from scratch.

---

## 3. Variable-Size Window (Find Max/Min Length)

Shrink only when the window becomes **invalid**.

```python
# Longest substring with at most k distinct characters
def longest_at_most_k(s, k):
    from collections import Counter
    freq = Counter()
    left = 0
    best = 0

    for right in range(len(s)):
        freq[s[right]] += 1

        while len(freq) > k:          # too many distinct chars
            freq[s[left]] -= 1
            if freq[s[left]] == 0:
                del freq[s[left]]
            left += 1

        best = max(best, right - left + 1)

    return best
```

---

## 4. Variable-Size Window (Find Min Length)

Shrink eagerly — every valid window is a candidate for the minimum.

```python
# Minimum subarray sum >= target
def min_subarray_sum(arr, target):
    left = 0
    total = 0
    best = float('inf')

    for right in range(len(arr)):
        total += arr[right]

        while total >= target:        # valid → try to shrink
            best = min(best, right - left + 1)
            total -= arr[left]
            left += 1

    return best if best != float('inf') else 0
```

**Pattern:** `max` window → shrink only when **invalid**. `min` window → shrink whenever **valid**.

---

## 5. Frequency Map Window (Character Problems)

Use `Counter` or a size-26 array for letter tracking.

```python
# Longest substring without repeating characters
def longest_unique(s):
    seen = set()
    left = 0
    best = 0

    for right in range(len(s)):
        while s[right] in seen:       # duplicate found → shrink
            seen.discard(s[left])
            left += 1
        seen.add(s[right])
        best = max(best, right - left + 1)

    return best
```

---

## 6. Permutation / Anagram Matching

Find all anagrams of `p` in `s` — fixed window + frequency comparison.

```python
from collections import Counter

def find_anagrams(s, p):
    need = Counter(p)
    have = Counter()
    left = 0
    result = []

    for right in range(len(s)):
        have[s[right]] += 1

        if right - left + 1 > len(p):  # window too big
            have[s[left]] -= 1
            if have[s[left]] == 0:
                del have[s[left]]
            left += 1

        if have == need:                # match found
            result.append(left)

    return result
```

### Optimization: Compare Counts Without Full Dict Equality

```python
# Track how many characters have matching counts
formed = sum(1 for c in need if have.get(c, 0) == need[c])
required = len(need)

# Update formed when a character's count crosses the threshold
```

This avoids O(26) dict comparison on every step → O(1) per step.

---

## 7. Two-Pointer vs Sliding Window

| | Two-Pointer | Sliding Window |
|---|---|---|
| **Direction** | Left moves right, right moves left | Both move right |
| **Goal** | Find pairs, triplets, or symmetric targets | Subarray/substring constraints |
| **State** | Usually just the sum | Frequency map, sum, count, etc. |
| **Shrink** | Only when sum too big (sum-to-target) | `while` loop with validity check |

**Rule of thumb:** If both ends move in the **same direction** → sliding window.

---

## 8. Common Pitfalls

1. **Forgetting to shrink before recording answer** — the window might be invalid when you update `result`.
2. **Off-by-one on window size** — use `right - left + 1` for inclusive window length.
3. **Not cleaning up the frequency map** — deleting keys when count hits 0 prevents stale comparisons.
4. **Using a set instead of a frequency map** — when duplicates matter (e.g., "at most k"), a set loses count info.
5. **O(n²) by recalculating sum** — use the running sum trick (add right, drop left).

---

## 9. Cheat Sheet: Which Pattern to Use

| Problem Type | Window | Shrink When |
|---|---|---|
| Max subarray sum of size k | Fixed | Slide (no shrink) |
| Longest substring with ≤ k distinct | Variable, max | Invalid (too many distinct) |
| Shortest subarray with sum ≥ target | Variable, min | Valid (≥ target) |
| Longest without repeating chars | Variable, max | Duplicate found |
| All anagrams of p in s | Fixed (= len(p)) | Window exceeds len(p) |
| Min window substring containing all of t | Variable, min | Window contains all of t |
