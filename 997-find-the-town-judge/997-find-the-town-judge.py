class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        Trust=[]
        for i in range(n):
            Trust.append([0,0])
        for i in trust:
            a,b=i[0]-1,i[1]-1
            Trust[a][0]+=1
            Trust[b][1]+=1
        #print(Trust)
        for i in range(len(Trust)):
            if Trust[i][0]==0 and Trust[i][1]==n-1:
                return i+1
        return -1