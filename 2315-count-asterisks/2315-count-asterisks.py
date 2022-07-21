class Solution:
    def countAsterisks(self, st: str) -> int:
        s=True
        count=0
        for i in st:
            if i=='|' and s:
                s=False
            elif not s and i=='|':
                s=True
            if s and i=='*':
                count+=1
        return count