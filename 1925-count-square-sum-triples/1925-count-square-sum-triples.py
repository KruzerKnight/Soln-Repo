class Solution:
    def countTriples(self, n: int) -> int:
        count=0
        for i in range(1,n):
            for j in range(i+1,n):
                r=(i**2+j**2)**0.5
               # print(i,j,r)
                if r<=n and r==round(r):
                    count+=2
        return count