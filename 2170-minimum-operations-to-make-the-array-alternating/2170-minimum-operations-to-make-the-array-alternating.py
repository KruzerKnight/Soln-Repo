class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        even = Counter(nums[i] for i in range(0, n, 2))
        odd = Counter(nums[i] for i in range(1, n, 2))
        even[inf] = 0
        odd[-inf] = 0
        e, ce = max(even.items(), key=lambda item:item[1])
        o, co = max(odd.items(), key=lambda item:item[1])
        if e != o:
            return n - ce - co
        even.pop(e)
        odd.pop(o)
        ce1 = max(even.values())
        co1 = max(odd.values())
        return n - max(ce1 + co, ce + co1)
# class Solution:
#     def minimumOperations(self, a: List[int]) -> int:
#         c = list(Counter(a[0::2]).most_common(3))
#         d = list(Counter(a[1::2]).most_common(3))
#         c += [(0, 0), (-1, 0)]
#         d += [(0, 0), (-1, 0)]
#         z = len(a)
#         for cv, cc in c:
#             for dv, dc in d:
#                 if cv != dv:
#                     z = min(z, len(a) - cc - dc)
#         return z