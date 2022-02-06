class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        for i in nums:
            if(count<2 or i!=nums[count-1] or i!=nums[count-2]): #to check no of its appearance
                nums[count]=i
                count+=1
        return count