class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res=start
        for i in range(1,n):
            cur=start+2*i
            res=res^cur
        return res