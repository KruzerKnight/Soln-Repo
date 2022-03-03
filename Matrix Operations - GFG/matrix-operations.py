#User function Template for python3

class Solution:
    def endPoints(self, matrix, n, m):
        ##code here
        i,j=0,0
        out=1
        d=1
        while(out):
            if i<n and i>=0 and j>=0 and j<m:
                if matrix[i][j]==1:
                    matrix[i][j]=0
                    if d==1:
                       d=2
                    elif d==2:
                        d=3
                    elif d==3:
                        d=4
                    else:
                        d=1
                if d==1:
                    j+=1
                elif d==2:
                    i+=1
                elif d==3:
                    j-=1
                elif d==4:
                    i-=1
            
            else:
                if j>=m or j<0:
                    if j>0:
                        return [i,j-1]
                    else:
                        return [i,j+1]
                else:
                    if i>0:
                        return [i-1,j]
                    else:
                        return [i+1,j]
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        matrix = []
        for i in range(r):
            line = [int(x) for x in input().strip().split()]
            matrix.append(line)
        ob = Solution()
        ans = ob.endPoints(matrix,r,c)
        print('(',ans[0],', ',ans[1],')',sep ='')

# } Driver Code Ends