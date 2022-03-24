class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count=0
        s=0
        l=[]
        for i in people:
            if i>=limit:
                count+=1
            else:
                l.append(i)
        #print(l)
        i=0
        j=len(l)-1
        l.sort()
        while(i<=j):
            if (l[i]+l[j])<=limit:
                i+=1
            j-=1
            count+=1
        return count
    
#solution without using another list takes double the time