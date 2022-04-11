class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count=0
        for i in range(0,len(flowerbed)):
            if (i==0 or flowerbed[i-1]==0) and flowerbed[i]==0 and (i==len(flowerbed)-1 or flowerbed[i+1]==0):
                count+=1
                flowerbed[i]=1
        #
        if count>=n:
            return True
        return False
    
    
#     class Solution(object):
#     def canPlaceFlowers(self, flowerbed, n):
#         zeros, ans = 1, 0  # Easier handling of prefixes, just initialize zeros to 1
#         for f in flowerbed:
#             if f == 0: 
#                 zeros += 1
#             else:
#                 ans += (zeros - 1) // 2
#                 zeros = 0
#         return ans + zeros // 2 >= n  # Note that suffix zeros need not -1
# class Solution(object):
#     def canPlaceFlowers(self, F, n):
#         return sum((len(zeros) - 1) // 2 for zeros in ''.join(map(str, [0] + F + [0])).split('1')) >= n