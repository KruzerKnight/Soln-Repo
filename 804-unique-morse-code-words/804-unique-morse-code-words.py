class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        l=[]
        a=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for i in words:
            r=''
            for j in i:
                r+=a[ord(j)-ord('a')]
            l.append(r)
        return len(set(l))
        