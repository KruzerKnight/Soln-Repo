# https://leetcode.com/problems/verifying-an-alien-dictionary/discuss/361525/Python-Solution-with-Detailed-Explaination-for-Beginner
    
# Arigato :)

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d={}
        new_words=[]
        
        for i,ch in enumerate(order):
            d[ch]=i
        
        for i in words:
            new=[]
            for j in i:
                new.append(d[j])
            new_words.append(new)
            
        for i,j in zip(new_words,new_words[1:]):
            if i>j:
                return False
        return True