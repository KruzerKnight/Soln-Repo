class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            s[i],s[-1-i]=s[-1-i],s[i]
 # same without negative indexing and faster
# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         mid = len(s) // 2
#         l = len(s) - 1
#         for i in range(mid):
#             s[i], s[l] = s[l], s[i]
#             l -= 1
