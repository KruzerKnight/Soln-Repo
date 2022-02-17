class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        max1,max0=0,0
        count1,count0=0,0
        fl1,fl0=0,0
        for i in range(len(s)):
            if(s[i]=='1'):
                if not fl1:
                    fl0=0
                    fl1=1
                    max0=max(max0,count0)
                    count0=0
                    count1+=1
                else:
                    count1+=1
            else:
                if not fl0:
                    fl1=0
                    fl0=1
                    max1=max(max1,count1)
                    count1=0
                    count0+=1
                else:
                    count0+=1
        max0=max(max0,count0)
        max1=max(max1,count1)
        return max1>max0