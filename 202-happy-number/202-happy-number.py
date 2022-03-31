class Solution:
    def isHappy(self, n: int) -> bool:
        r=False
        l=[n]
        while(1):
            s=str(n)
            c=0
            
            for i in s:
                j=int(i)
                c+=j*j
            n=c
            
            if(c==1):
                r=True
                break
            if c in l:
                break
            l.append(c)
        return(r)