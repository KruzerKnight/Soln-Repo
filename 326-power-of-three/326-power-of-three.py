class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        i=0
        st=1
        while(st<=n):
            st=3**i
            if(st==n):
                return True
            i+=1