class Solution:
    def largestGoodInteger(self, num: str) -> str:
        r=-1
        count=0
        for i in range(1,len(num)):
            if num[i]==num[i-1]:
                count+=1
            else:
                count=0
            #print(i,r,num[i],num[i-1])
            if count==2:
                r=max(r,int(num[i]))
                count=0
        if r==-1:
            return ''
        return str(r)*3