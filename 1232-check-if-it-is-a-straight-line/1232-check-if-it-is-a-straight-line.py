class Solution:
    def checkStraightLine(self, c: List[List[int]]) -> bool:
        if c[0][0]==c[1][0]:
            for i in range(2,len(c)):
                if c[i][0]!=c[0][0]:
                    return False
            return True
        slope=(c[1][1]-c[0][1])/(c[1][0]-c[0][0])
        for i in range(2,len(c)):
            if(c[i][0]-c[0][0])==0:
                return False
            if slope!=(c[i][1]-c[0][1])/(c[i][0]-c[0][0]):
                return False
        return True