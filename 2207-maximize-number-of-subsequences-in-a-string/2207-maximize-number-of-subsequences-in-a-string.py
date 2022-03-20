class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        c1 = text.count(pattern[0])
        c2 = text.count(pattern[1])
        ans = max(c1, c2)
        cnt = 0
        for c in text:
            if c == pattern[1]:
                ans += cnt
            if c == pattern[0]:
                cnt += 1
        return ans