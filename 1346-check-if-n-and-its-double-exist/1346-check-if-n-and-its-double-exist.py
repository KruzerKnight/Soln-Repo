class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            if 2*arr[i] in arr[:i] or 2*arr[i] in arr[i+1:]:
                return True
        return False
    
    
    # alternate solutions
    
#     class Solution:
#     def checkIfExist(self, arr: List[int]) -> bool:
#         cnt_dict = dict()
#         for x in arr:
#             cnt_dict[x] = cnt_dict[x] + 1 if x in cnt_dict else 1
#         for x in arr:
#             if x * 2 in cnt_dict:
#                 if x != 0 or cnt_dict[0] >= 2:
#                     return True
#         return False
    
    
#     class Solution:
#   def checkIfExist(self, arr: List[int]) -> bool:
    
#     s = collections.Counter(arr)
    
#     #check if there are more than one zeros
#     if(s[0]>1): return True;
    
    
#     for num in arr:
#       if s[2*num] and num!=0:
#         return True
#     return False



# class Solution:
#     def checkIfExist(self, arr: List[int]) -> bool:
#         hashmap = {}
#         for el in arr:
#             if hashmap.get(el/2, False) or hashmap.get(el*2, False):
#                 return True
#             hashmap[el] = hashmap.get(el, 0) + 1  
#         return False
