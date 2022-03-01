#User function Template for python3
class Solution:
    def countPairs(self, N, X, numbers): 
        #code here
        X=str(X)
        x=len(X)
        count=0
        d={}
        for j in numbers:
            i=str(j)
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in range(len(X)):
            f=X[:i]
            r=X[i:]
            #print(d,f,r)
            if f in d and r in d:
                #print(f,r)
                if f==r:
                    count+=((d[f]-1)*d[r])
                else:
                    count+=d[f]*d[r]
        return count
#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N,X = map(int,input().strip().split())
        numbers = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.countPairs(N, X, numbers)
        print(ans)


# } Driver Code Ends