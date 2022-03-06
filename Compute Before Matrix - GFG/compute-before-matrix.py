#User function Template for python3

class Solution:
    def computeBeforeMatrix(self, N, M, after):

        
        for i in range(N-1,0,-1):
            for j in range(M):
                after[i][j] -= after[i-1][j]
                
        for i in range(N):
            for j in range(M-1,0,-1):
                after[i][j] -= after[i][j-1]
                
        return after
        
# Question and testcases are a bit different. In this the Every element is sum of rows and columns and before it. So the approach I followed here is
# 1. Subtract each value by the element in the before column

# 2. Subtract each value by the element in the before row.

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    
    T = int(input())
    while T > 0: 
        N, M =[int(i) for i in input().split()]
        after= []
        for j in range (N):
            after.append([int(i) for i in input().split()])
        ob = Solution()
        before=ob.computeBeforeMatrix(N,M,after)
        for i in range(len(before)): 
            for j in range(len(before[i])):
                print(before[i][j],end=' ')
            print()
        
        
        T -= 1
# } Driver Code Ends