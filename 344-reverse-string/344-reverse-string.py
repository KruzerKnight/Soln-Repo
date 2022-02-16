class Solution:
    def reverseString(self, s: List[str]) -> None:
        mid = len(s) // 2
        l = len(s) - 1
        for i in range(mid):
            s[i], s[l] = s[l], s[i]
            l -= 1