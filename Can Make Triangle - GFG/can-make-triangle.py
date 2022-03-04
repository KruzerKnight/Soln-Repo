#User function Template for python3
class Solution:
    def canMakeTriangle(self, A, N): 
        #code here
        l=[]
        for i in range(N-2):
            a=A[i]
            b=A[i+1]
            c=A[i+2]
            if a<b+c and b<c+a and c<a+b:
                l.append(1)
            else:
                l.append(0)
        return l

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.canMakeTriangle(A, N)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends