class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        l=[[]]
        x=[]
        temp=[]
        n=len(nums)
        for i in range(1,2**n):
            x.append(bin(i)[2:])
        for i in x:
            temp=[]
            y=i[::-1]
            for j in range(len(i)):
                if int(y[j]):
                    temp.append(nums[j])
            l.append(temp)
        return l
    
    #faster solution
#     class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         def backtrack(lst, start):
#             res.append(list(lst))
            
#             for i in range(start, len(nums)):
#                 lst.append(nums[i])
                
#                 backtrack(lst, i+1)
#                 lst.pop()
            
#         backtrack([],  0)
#         return res
