class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        r=sentence.split()
        vow='aeiouAEIOU'
        for i in range(len(r)):
            if r[i][0] in vow:
                r[i]=r[i]+'ma'+'a'*(i+1)
            else:
                r[i]=r[i][1:]+r[i][0]+'ma'+'a'*(i+1)
        return ' '.join(r)