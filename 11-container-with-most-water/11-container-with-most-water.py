class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j=0,len(height)-1
        water=0
        while i<j:
            water=max(water,min(height[i],height[j])*(j-i))
            if height[i]>height[j]:
                j-=1
            else:
                i+=1
        return water