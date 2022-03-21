class Solution:
    def trap(self, height: List[int]) -> int:
        i,j=0,len(height)-1
        water=0
        maxl,maxr=0,0
        while i<j:
            if height[i]<height[j]:
                maxl=max(maxl,height[i])
                water+=maxl-height[i]
                i+=1
            else:
                maxr=max(maxr,height[j])
                water+=maxr-height[j]
                j-=1
        return water