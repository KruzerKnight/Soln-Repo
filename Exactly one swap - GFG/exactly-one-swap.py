#User function Template for python3
class Solution:
    def countStrings(self, s): 
        #code here
        d={}
        res=0
        n=len(s)
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        m=max(d.values())
        for i in range(n):
            d[s[i]]-=1
            res+=n-1-i-d[s[i]]
        if(m>1):
            return res+1
        return res
#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        S = input()
        ob = Solution()
        ans = ob.countStrings(S)
        print(ans)
# } Driver Code Ends