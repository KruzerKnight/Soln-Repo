class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies)<k:
            return 0
        elif sum(candies)==k:
            return 1
        left,right=0,sum(candies)//k
        while left<right:
            mid=(left+right+1)//2
            if k>sum(a//mid for a in candies):
                right=mid-1
            else:
                left=mid
        return left
    
#     Assume we want give each child m candies, for each pile of candies[i],
# we can divide out at most candies[i] / m sub piles with each pile m candies.

# We can sum up all the sub piles we can divide out, then compare with the k children.

# If k > sum,
# we don't allocate to every child,
# since the pile of m candidies it too big,
# so we assign right = m - 1.

# If k <= sum,
# we are able to allocate to every child,
# since the pile of m candidies is small enough
# so we assign left = m.

# We repeatly do this until left == right, and that's the maximum number of candies each child can get.


# Tips
# Tip1. left < right Vs left <= right

# Check all my solution, I keep using left < right.
# The easy but important approach:
# follow and upvote my codes,
# try to do the same.
# you'll find all binary search is similar,
# never bother thinking it anymore.

# Tip2. mid = (left + right + 1) / 2 Vs mid = (left + right) / 2

# mid = (left + right) / 2 to find first element valid
# mid = (left + right + 1) / 2to find last element valid
