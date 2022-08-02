class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        m=len(isConnected)
        n=len(isConnected[0])
        seen=set()
        
        def dfs(node):
            for n, adj in enumerate(isConnected[node]):
                if adj and n not in seen:
                    seen.add(n)
                    dfs(n)
        ans = 0
        for i in range(m):
            if i not in seen:
                dfs(i)
                ans += 1
        return ans