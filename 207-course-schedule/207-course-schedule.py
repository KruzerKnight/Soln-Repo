class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n=numCourses
        d=defaultdict(list)
        indegree=[0]*n
        #print(indegree)
        for i,j in prerequisites:
            d[i].append(j)
            indegree[j]+=1
        #print(indegree)
        q=[]  
        for i in range(n):
            if indegree[i]==0:
                q.append(i)
        
        for i in q:
            for j in d[i]:
                indegree[j]-=1
                if indegree[j]==0:
                    q.append(j)
        #print(q)
        if len(q)==n:
            return True
        return False