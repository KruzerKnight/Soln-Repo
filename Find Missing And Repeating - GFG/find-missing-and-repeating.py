#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        l=[0]*(n+1)
        r=n
        m=n
        for i in arr:
            l[i]+=1
        for j in range(1,n):
            if l[j]==2:
                r=j
            if l[j]==0:
                m=j
        return(r,m)
        
        
# # Python3 program to find the repeating 
# # and missing elements 

# # The output of this function is stored 
# # at x and y 
# def getTwoElements(arr, n):
    
#     global x, y
#     x = 0
#     y = 0
    
#     # Will hold xor of all elements 
#     # and numbers from 1 to n 
#     xor1 = arr[0]
    
#     # Get the xor of all array elements
#     for i in range(1, n):
#         xor1 = xor1 ^ arr[i]
        
#     # XOR the previous result with numbers 
#     # from 1 to n
#     for i in range(1, n + 1):
#         xor1 = xor1 ^ i
    
#     # Will have only single set bit of xor1
#     set_bit_no = xor1 & ~(xor1 - 1)
    
#     # Now divide elements into two 
#     # sets by comparing a rightmost set 
#     # bit of xor1 with the bit at the same 
#     # position in each element. Also, 
#     # get XORs of two sets. The two 
#     # XORs are the output elements. 
#     # The following two for loops 
#     # serve the purpose
#     for i in range(n):
#         if (arr[i] & set_bit_no) != 0:
            
#             # arr[i] belongs to first set
#             x = x ^ arr[i]
#         else:
            
#             # arr[i] belongs to second set
#             y = y ^ arr[i]
            
#     for i in range(1, n + 1):
#         if (i & set_bit_no) != 0:
            
#             # i belongs to first set
#             x = x ^ i
#         else:
            
#             # i belongs to second set
#             y = y ^ i 
        
#     # x and y hold the desired 
#     # output elements 
    
# # Driver code
# arr = [ 1, 3, 4, 5, 5, 6, 2 ]
# n = len(arr)
    
# getTwoElements(arr, n)

# print("The missing element is", x,
#       "and the repeating number is", y)
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends