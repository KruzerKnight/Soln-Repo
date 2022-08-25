class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        l=1
        n=len(arr)
        ans=0
        while l<=n:
            for i in range(n-l+1):
                #print(arr[i:i+l])
                ans+=sum(arr[i:i+l])
            l+=2
        return ans