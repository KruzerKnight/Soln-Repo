class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        while(l<r):
            mid=(l+r)//2
            if nums[mid]>nums[r]:
                l=mid+1
            elif nums[mid]<nums[l]:
                r=mid
                l+=1
            else:
                r-=1
        return nums[l]
    
    # similar to find minimum in roated sorted array
#     since if nums[mid]<nums[l] then nums[l] surely wouldn't be the smallest element
#     thus we increase it by 1, that is moving from it
    
#     else is for (nums[l] <= nums[mid] <= nums[r] )
#     so r-=1 so we reduce the right element by 1