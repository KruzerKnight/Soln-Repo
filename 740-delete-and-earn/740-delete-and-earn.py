class Solution(object):
    def deleteAndEarn(self, nums):
        points, prev, curr = [0] * 10001, 0, 0
        for num in nums:
            points[num] += num
        for value in points:
            prev, curr = curr, max(prev + value, curr)
        return curr
        
# The order of nums does not matter.
# Once we decide that we want a num, we can add all the occurrences of num into the total.
# We first transform the nums array into a points array that sums up the total number of points for that particular value. A value of x will be assigned to index x in points.

# nums: [2, 2, 3, 3, 3, 4] (2 appears 2 times, 3 appears 3 times, 4 appears once)
# points: [0, 0, 4, 9, 4] <- This is the gold in each house!

# The condition that we cannot pick adjacent values is similar to the House Robber question that we cannot rob adjacent houses. Simply pass points into the rob function for a quick win \U0001f31d!