#User function Template for python3

class Solution:
    def partyHouse(self, N, adj):
        # code here
        #find distance of each node from each node and then calculate the 
        #minimum of all the maximums
        
        def dfs(curr,prev,dep):
            maxdep[0] = max(maxdep[0],dep)
            for edge in adj[curr]:
                if edge != prev:
                    dfs(edge,curr,dep+1)
        
        ans = 999999999
        for i in range(1,N+1):
            maxdep = [0]
            dfs(i,-1,0)
            ans = min(ans,maxdep[0])
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        adj = [[] for x in range(N+1)]
        for i in range(N-1):
            x, y = [int(a) for a in input().split()]
            adj[x].append(y)
            adj[y].append(x)
        
        ob = Solution()
        print(ob.partyHouse(N, adj))
# } Driver Code Ends