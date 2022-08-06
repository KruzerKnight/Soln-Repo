class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        #https://leetcode.com/problems/permutations/discuss/993970/Python-4-Approaches-%3A-Visuals-%2B-Time-Complexity-Analysis
        
        def rec(num,perm=[],res=[]):
            if not num:
                res.append(perm[::])
            for i in range(len(num)):
                l=num[:i]+num[i+1:]
                perm.append(num[i])
                rec(l,perm,res)
                perm.pop()
            return res
        return rec(nums)

    