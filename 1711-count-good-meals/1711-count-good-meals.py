class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        ans=0
        freq=defaultdict(int)
        for item in deliciousness:
            for i in range(22):
                ans+=freq[2**i-item]
            freq[item]+=1
        return ans%(10**9+7)
            