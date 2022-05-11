class Solution:
    
    def countVowelStrings(self, n: int) -> int:        
        dp = [1] * 5
        
        for i in range(2, n+1):
            for j in range(4, -1, -1):
                dp[j] += sum(dp[:j])            
        
        return sum(dp)
    #https://leetcode.com/problems/count-sorted-vowel-strings/discuss/2027288/Python-4-approaches-(DP-Maths)