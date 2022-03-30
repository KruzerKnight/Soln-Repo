class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        first=list(words[0])
        for i in words:
            r=[]
            for j in i:
                if j in first:
                    r.append(j)
                    first.remove(j)
            first=r
        return first
    
    # we are choosing first word then comparing it with other word, we store the common words instead of first and check with other words