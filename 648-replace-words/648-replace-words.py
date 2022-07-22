class Solution:
    def replaceWords(self, di: List[str], sentence: str) -> str:
        di.sort()
        l=sentence.split(' ')
        
        for i in range(len(l)):
            for j in range(len(di)):
                n=len(di[j])
                if di[j] == l[i][:n]:
                    l[i]=di[j]
                    break
        
        return ' '.join(l)