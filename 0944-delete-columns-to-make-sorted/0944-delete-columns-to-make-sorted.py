class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        r=['' for _ in range(len(strs[0]))]
        for i in range(len(strs)):
            for j in range(len(strs[i])):
                r[j]+=strs[i][j]
        ans=0
        for i in range(len(r)):
            if ''.join(sorted(r[i]))!=r[i]:
                ans+=1
        return ans