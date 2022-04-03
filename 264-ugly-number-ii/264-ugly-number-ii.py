class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ug=[0]*n
        
        ug[0]=1
        n2=2
        n3=3
        n5=5
        
        i2=i3=i5=0
        
        for i in range(1,n):
            ug[i]=min(n2,n3,n5)
            
            if ug[i]==n2:
                i2+=1
                n2=ug[i2]*2
            if ug[i]==n3:
                i3+=1
                n3=ug[i3]*3
            if ug[i]==n5:
                i5+=1
                n5=ug[i5]*5
        return ug[-1]