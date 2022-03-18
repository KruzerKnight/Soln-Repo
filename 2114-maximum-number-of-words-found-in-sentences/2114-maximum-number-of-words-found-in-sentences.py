class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxi=0
        for i in sentences:
            l=list(i.split())
            maxi=max(maxi,len(l))
        return maxi