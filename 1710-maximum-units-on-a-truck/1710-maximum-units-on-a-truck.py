class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1],reverse=True)
        r=0
        for i in boxTypes:
            if truckSize-i[0]>=0:
                r+=i[1]*i[0]
                truckSize-=i[0]
            else:
                r+=i[1]*truckSize
                return r
            #print(i,r)
        return r