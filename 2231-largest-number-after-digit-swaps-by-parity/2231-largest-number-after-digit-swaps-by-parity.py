class Solution:
    def largestInteger(self, num: int) -> int:
        l=list(str(num))
        odd=[]
        even=[]
        for i in range(len(l)):
            if int(l[i])%2==0:
                even.append(l[i])
                l[i]='0'
            else:
                odd.append(l[i])
                l[i]='1'
        odd.sort()
        even.sort()
        for i in range(len(l)):
            if l[i]=='1' and odd:
                l[i]=odd.pop()
            elif even:
                l[i]=even.pop()
        return int(''.join(l))