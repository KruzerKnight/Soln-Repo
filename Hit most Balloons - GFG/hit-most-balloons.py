#User function Template for python3
def slope(p1,p2):
    if p1[0]==p2[0]:
        return 'y'
    return float(p1[1]-p2[1])/float(p1[0]-p2[0])

class Solution: 
    def mostBalloons(self, N, arr):
        # Code here
        if len(arr)==2:
            return 2
        maxi=0
        for i in arr:
            count=0
            dup=0
            d={}
            for j in arr:
                if(i==j):
                    dup+=1
                    continue
                s=slope(i,j)
                if s in d:
                    d[s]+=1
                else:
                    d[s]=1
            maxi=max(maxi,max(d.values())+dup)
        return maxi

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__':
    
    T = int(input())
    while T > 0: 
        N = int(input()) 
        arr=[[] for j in range(N)]
        for j in range(2): 
            inp = [int(i) for i in input().split()] 
            for i in range(N): 
                arr[i].append(inp[i])
        ob = Solution()
        print(ob.mostBalloons(N, arr))
        
        T -= 1
# } Driver Code Ends