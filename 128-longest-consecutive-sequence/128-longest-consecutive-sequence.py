class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxi=0
        snum=set(nums)
        for i in nums:
            if i-1 in snum:
                continue
            nxt=i
            while nxt+1 in snum:
                nxt+=1
            maxi=max(maxi,nxt-i+1)
        return maxi