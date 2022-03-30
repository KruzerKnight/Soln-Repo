class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count=0
        d1=defaultdict(lambda: 0)
        for i in words1:
            d1[i]+=1
        d2=defaultdict(lambda: 0)
        for i in words2:
            d2[i]+=1
        
        if len(words2)>len(words1):
            for i in words1:
                if d1[i]==1 and d2[i]==1:
                    count+=1
        else:
            for i in words2:
                if d1[i]==1 and d2[i]==1:
                    count+=1
                    
        return count
    
    #we count using dictinoary and check if both sides count are 1, if yes then increase the variable count