class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        string=(s+s)[1:-1]
        return string.find(s)!=-1