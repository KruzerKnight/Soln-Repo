#User function Template for python3
class Solution:
    #learnnnnnnnnnnnnnnnnnn
    def stringPartition(ob,S,a,b):
        for pos in range (1, len(S)):
            if not int(S[:pos]) % a and not int(S[pos:]) % b:
                return S[:pos] + " " + S[pos:]
        return -1
    #     def stringPartition(ob,S,a,b):
    #   anslist = []
    #   i = 0
    #   for i in range(len(S)-1):
    #       tempString = S[0:i+1]
    #       if int(tempString)%a == 0:
    #           if int(S[i+1:])%b == 0:
    #               anslist.append([tempString,S[i+1:]])
    #   if len(anslist) == 0:
    #       return -1
    #   anslist = sorted(anslist,key=lambda x: int(x[0][0]))
    #   str = anslist[0][0] + " " + anslist[0][1]
    #   return str


#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S,a,b=map(str,input().strip().split(" "))
        a=int(a)
        b=int(b)
        ob = Solution()
        print(ob.stringPartition(S,a,b))
# } Driver Code Ends