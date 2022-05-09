#User function Template for python3

class Solution:
	def findProb(self, N, start_x, start_y, steps):
		# Code here
		
		def issafe(r,c):
		    if r>=0  and r < N and c>=0 and c < N :
		        return True
		    return False
		curr = [[0 for i in range(N)] for j in range(N)]
		nex = [[0 for i in range(N)] for j in range(N)]
		moves = [[2,1],[2,-1],[-2,-1],[-2,1],[1,2],[-1,2],[1,-2],[-1,-2]]
		
		curr[start_x][start_y] = 1
		for k in range(steps):
		    for i in range(N):
		        for j in range(N):
		            ni = 0 
		            nj = 0
		            if curr[i][j] != 0 :
		                for move in moves:
		                    ni = i+move[0]
		                    nj = j+ move[1]
		                    if issafe(ni,nj):
		                        nex[ni][nj] += curr[i][j]/8
		            curr[i][j] = 0
	        curr = nex
	        nex = [[0 for i in range(N)] for j in range(N)]
	    #print(curr)
	    ans = 0
	    for i in range(N):
	        for j in range(N):
	            ans+= curr[i][j]
	    return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N, start_x, start_y, steps = input().split()
		N = int(N)
		start_x = int(start_x)
		start_y = int(start_y)
		steps = int(steps)
		ob = Solution()
		ans = ob.findProb(N, start_x, start_y, steps)
		print('%.6f'%ans)
# } Driver Code Ends