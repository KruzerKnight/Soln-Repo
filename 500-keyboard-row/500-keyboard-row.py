class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1="qwertyuiopQWERTYUIOP"
        row2="asdfghjklASDFGHJKL"
        row3="zxcvbnmZXCVBNM"
        l=[]
        for i in words:
            if(i[0] in row1):
                fl=1
                for j in row2+row3:
                    if j in i:
                        fl=0
                        break
                if(fl):
                    l.append(i)
            if(i[0] in row2):
                fl=1
                for j in row1+row3:
                    if j in i:
                        fl=0
                        break
                if(fl):
                    l.append(i)
            if(i[0] in row3):
                fl=1
                for j in row2+row1:
                    if j in i:
                        fl=0
                        break
                if(fl):
                    l.append(i)
        return l