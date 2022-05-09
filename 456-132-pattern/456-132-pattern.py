class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        te=float(-inf)
        stack=[]
        for i in range(len(nums)-1,-1,-1):
            if nums[i]<te:
                return True
            while stack and stack[-1]<nums[i]:
                te=stack.pop()
            
            stack.append(nums[i])
        return False
    
# class Solution:
    
#     def find132pattern(self, nums):
#         stack, s3 = [], -float("inf")
#         for n in nums[::-1]:
#             if n < s3: return True
#             while stack and stack[-1] < n: s3 = stack.pop()
#             stack.append(n)
#         return False
    
    
# #     My understanding:
# # You go from the right side, and find the first element that is bigger than one or more elements that are further to the right. If that happens, you want to find the biggest number that is smaller than the current element. You do that by popping out all of those smaller elements.

# # Why you want to find the biggest number that is smaller than the current element? Because you want to maximize the chance that you find something smaller than the number going left. If you find such smaller one, then return True.
# # Note that the elements in the stack are stored in descending order, all elements that are append to the stack are smaller than what's already in the stack. This is important, since we want to guarantee that the last element that we pop out of the stack is the biggest value that is smaller than the current value.