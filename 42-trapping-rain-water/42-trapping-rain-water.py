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
    
#     instead of calculating area by height*width, we can think it in a cumulative way. In other words, sum water amount of each bin(width=1).
# Search from left to right and maintain a max height of left and right separately, which is like a one-side wall of partial container. Fix the higher one and flow water from the lower part. For example, if current height of left is lower, we fill water in the left bin. Until left meets right, we filled the whole container.
