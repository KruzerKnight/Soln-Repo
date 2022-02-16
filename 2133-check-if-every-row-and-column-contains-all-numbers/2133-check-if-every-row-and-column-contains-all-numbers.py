class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n=len(matrix)
        for i in matrix:
            if(len(set(i)))!=n:
                return False
        l=[]
        for i in matrix:
            ad=[[x,i] for i,x in enumerate(i)]
            l+=ad
        l=sorted(l, key= lambda x:x[1])
        for j in range(n):
            count=0
            s=set()
            for k in range(j*n,(j+1)*n):
                i=l[k]
                if i[1]==j:
                    s.add(i[0])
            if(len(s)!=n):
                return False
        return True