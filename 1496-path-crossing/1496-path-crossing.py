class Solution:
    def isPathCrossing(self, path: str) -> bool:
        p=[0,0]
        s=set()
        q=[str(p[0]),'-',str(p[1])]
        s.add(''.join(q))
        for i in path:
            if i=='N':
                p[1]+=1
            elif i=='S':
                p[1]-=1
            elif i=='W':
                p[0]-=1
            elif i=='E':
                p[0]+=1
            q=[str(p[0]),'-',str(p[1])]
            #print(i,p,q,s)
            if ''.join(q) in s:
                return True
            else:
                s.add(''.join(q))
        return False