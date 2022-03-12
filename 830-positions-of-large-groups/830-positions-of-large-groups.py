class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        prev=s[0]
        count=0
        j=0
        l=[]
        for i in range(1,len(s)):
            if s[i]==prev:
                count+=1
            else:
                prev=s[i]
                if(count>=2):
                    l.append([j,i-1])
                j=i
                count=0
        if(count>=2):
                    l.append([j,i])
        return l
                