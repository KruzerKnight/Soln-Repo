class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        d={x:i for i,x in enumerate(row)}
        count=0
        for i in range(len(row)):
            p1=row[i]
            if p1%2==0:
                p2=p1+1
            else:
                p2=p1-1
            j=d[p2]
            if j-i>1:
                row[i+1],row[j]=row[j],row[i+1]
                d[row[i+1]]=i+1
                d[row[j]]=j
                count+=1
        return count