class Solution:
    def calPoints(self, ops: List[str]) -> int:
        l=[]
        for i in ops:
            if i.isnumeric() or len(i)>=2:
                l.append(int(i))
            elif i=='+':
                l.append(l[-1]+l[-2])
            elif i=='D':
                l.append(l[-1]*2)
            elif i=='C':
                l.pop()
            #print(i,l)
        #print(l)
        return sum(l)