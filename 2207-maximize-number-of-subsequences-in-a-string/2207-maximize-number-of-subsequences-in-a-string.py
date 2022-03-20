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
    
    
#     Intuition
# If we add pattern[0], the best option is to add at the begin.
# If we add pattern[1], the best option is to add at the end.


# Explanation
# Firstly we'll try to find the number of subquence pattern in the current string text
# Iterate every character c from input string text,
# cnt1 means the count of character pattern[0],
# cnt2 means the count of character pattern[1].

# If c == pattern[1],
# it can build up string pattern with every pattern[0] before it,
# so we update res += cnt1 as well as cnt2++

# If c == pattern[0],
# we simply increment cnt1++.

# Then we consider of adding one more character:

# If we add pattern[0],
# the best option is to add at the begin,
# res += cnt2

# If we add pattern[1],
# the best option is to add at the end,
# res += cnt1


# Tip
# Use two if in my solution,
# to handle the corner case where pattern[0] == pattern[1].


# Complexity
# Time O(n)
# Space O(1)

#another solution

# def maximumSubsequenceCount(self, text, pattern):
#         res = cnt1 = cnt2 = 0
#         for c in text:
#             if c == pattern[1]:
#                 res += cnt1
#                 cnt2 += 1
#             if c == pattern[0]:
#                 cnt1 += 1
#         return res + max(cnt1, cnt2)
