class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        #grades.sort()
        n=len(grades)
        r=1
        ans=1
        for i in range(2,n):
            r+=i
            ans+=1
            #print(r,n)
            if r==n:
                return ans
            if r>n:
                return ans-1
        return ans