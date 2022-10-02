class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        m=min(a,b)
        c=0
        for i in range(1,m+1):
            if a%i==0 and b%i==0:
                # print(i)
                c+=1
        # if max(a,b)%m==0:
        #     c+=1
        return c