class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        d={}
        for i in range(len(graph)):
            d[i]=graph[i]
        n=len(graph)
        stack=[(0,[0])] #storing (node, and the path leading to it)
        res=[]
        while stack:
            node,path=stack.pop()
            
            if node==n-1:
                res.append(path)
                continue
            for i in d[node]:
                stack.append([i,path+[i]])
        return res