class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        d = deque([(nums[0],0)])
        for i in range(1, len(nums)):
            dp[i] = nums[i] + d[0][0]
            
            while d and d[-1][0] < dp[i]:   
                d.pop()                     # sliding window maximum variation
            d.append((dp[i],i))             # sliding window maximum variation
            
            if i-k == d[0][1]:              # sliding window maximum variation
                d.popleft()                 # sliding window maximum variation
                
        return dp[-1]