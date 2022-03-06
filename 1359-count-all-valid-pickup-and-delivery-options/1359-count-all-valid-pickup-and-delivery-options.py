class Solution:
    def countOrders(self, n):
        return (math.factorial(n * 2) >> n) % (10**9 + 7)
    
# Intuition 1
# Assume we have already n - 1 pairs, now we need to insert the nth pair.
# To insert the first element, there are n * 2 - 1 chioces of position。
# To insert the second element, there are n * 2 chioces of position。
# So there are (n * 2 - 1) * n * 2 permutations.
# Considering that delivery(i) is always after of pickup(i), we need to divide 2.
# So it's (n * 2 - 1) * n.


# Intuition 2
# We consider the first element in all 2n elements.
# The first must be a pickup, and we have n pickups as chioce.
# Its pair can be any position in the rest of n*2-1 positions.
# So it's (n * 2 - 1) * n.


# Intuition 3
# The total number of all permutation obviously eauqls to 2n!.
# For each pair, the order is determined, so we need to divide by 2.
# So the final result is (2n)!/(2^n)


# Complexity
# For each run, Time O(N), Space O(1).
# Also we can cache the result, so that O(1) amortized for each n.
# But in doesn't help in case of LC.
# Also we can pre calculate all results, so that we have O(N) space and O(1) time.


#Alternate Explanation:
# Idea
# Denote pickup 1, pickup 2, pickup 3, ... as A, B, C, ...
# Denote delivery 1, delivery 2, delivery 3, ... as a, b, c, ...
# We need to ensure a is behind A, b is behind B, ...

# This solution involves 2 stages.

# Stage 1
# We decide the order of all the pickups. It is trivial to tell there are n! possibilities
# Stage 2
# Given one possibility. Let's say the pickups are ordered like this A B C
# We can now insert the corresponding deliveries one by one.
# We start with the last pickup we made, namely, insert c, and there is only 1 valid slot.
# A B C c
# We continue with the second last pickup we made, namely, insert b, and there are 3 valid slots.
# A B x C x c x (where x denotes the location of valid slots for b)
# Let's only consider one case A B C c b. We continue with the third last pickup we made, namely, insert a, and there are 5 valid slots.


# Pickup possible value = n! (permutation)
# Delivery possible value = 135*..2n-1
# => (1×2×3×4×…(2\U0001d45b))/ (2×4×6×…×(2\U0001d45b))
# => (2\U0001d45b)! /(2^\U0001d45b)\U0001d45b!
# A x B x C x c x b x, (where x denotes the location of valid slots for a)
# In conclusion. we have in total 1 * 3 * 5 * ... * (2n-1) possibilities
# Thus, the final solution is n! * (1 * 3 * 5 * ... * (2n-1)) % 1000000007
# Complexity
# Time: O(n), can be improved to O(1) with memoization
# Space: O(1)