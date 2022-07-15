
class Solution:
    def minSum(self, arr, n):
        # Your code goes here
        arr.sort()
        if n==1:
            return arr[0]
        x1=arr[0::2]
        x2=arr[1::2]
        x1=[str(x) for x in x1]
        x2=[str(x) for x in x2]
        #print(x1,x2)
        x1=int(''.join(x1))
        x2=int(''.join(x2))
        return(x1+x2)
     # // sort the array -→ sorting is important to get minimum number at first
    #   sort(arr, arr + n);
       
    #   long long  int n1 = 0; 
    #   long long  int n2 = 0;
       
    #   for(int i=0; i<n; i++)
    #   {
    #       if(i & 1)
    #       {
    #           n1= n1 * 10 + arr[i];
    #       }
    #       else
    #       n2 = n2 * 10 + arr[i];
    #   }
    #   return n1+n2 ;

#{ 
#  Driver Code Starts

import heapq as hq

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        n = int(input())
        arr = [int(x) for x in input().split()]
        ob=Solution()
        print(ob.minSum(arr,n))

# } Driver Code Ends