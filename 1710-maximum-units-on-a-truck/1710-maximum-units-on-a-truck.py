class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        l=sorted(boxTypes, key=lambda x:x[1],reverse=True)
        units=0
        size=0
        for i in l:
            if(i[0]<=truckSize-size):
                units+=i[0]*i[1]
                size+=i[0]
            else:
                units+=(truckSize-size)*i[1]
                size+=truckSize-size
            if(size>truckSize):
                return units   
        return units