class Solution:
     def hasAllCodes(self, s, k):
        return len({s[i:i + k] for i in range(len(s) - k + 1)}) == 2 ** k

# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/discuss/2092441/Python-oror-2-Easy-oror-One-liner-with-explanation
