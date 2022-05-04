#User function Template for python3

class Solution:
   def permute(self,arr,n):
       sortlist = {}
       for i in range(n):
           sortlist[i+1] = arr[i][0]+arr[i][1]
       sorted_dt_value = sorted(sortlist.items(), key=lambda item: item[1])
       listarr = []
       for i in range(n):
           listarr.append(sorted_dt_value[i][0])
       return listarr
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

    
for _ in range(0,int(input())):
    n = int(input())
    arr = []
    for _ in range(0, n):
        ll = list(map(int, input().strip().split()))
        arr.append(ll)
    obj=Solution()
    ans = obj.permute(arr, n)
    for i in ans:
        print(i)
    



# } Driver Code Ends