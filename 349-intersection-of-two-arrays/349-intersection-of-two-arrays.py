class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=[]
        if len(nums1)>len(nums2):
            for i in nums2:
                if i in nums1:
                    l.append(i)
        else:
            for i in nums1:
                if i in nums2:
                    l.append(i)
        l=list(set(l))
        return l