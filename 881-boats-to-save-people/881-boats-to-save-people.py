class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count=0
        
        i=0
        j=len(people)-1
        people.sort()
        while(i<=j):
            if (people[i]+people[j])<=limit:
                i+=1
            j-=1
            count+=1
        return count
    
#this takes more time but less space but this is optimal