class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        fl=0
        for i in s:
            if i=='0':
                fl=1
            if i=='1' and fl:
                return False
        return True