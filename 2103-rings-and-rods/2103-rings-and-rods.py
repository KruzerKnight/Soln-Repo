class Solution:
    def countPoints(self, rings: str) -> int:
        count=0
        for i in range(10):
            
            r=0
            g=0
            b=0
            for j in range(0,len(rings),2):
                if rings[j]=='R' and r!=1:
                    if rings[j+1]==str(i):
                        r=1
                if rings[j]=='B' and b!=1:
                    if rings[j+1]==str(i):
                        b=1
                if rings[j]=='G' and g!=1:
                    if rings[j+1]==str(i):
                        g=1
                if r==1 and g==1 and b==1:
                    count+=1
                    break
        return count