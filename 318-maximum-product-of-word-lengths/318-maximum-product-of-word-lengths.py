class Solution:
    def maxProduct(self, words: List[str]) -> int:
        #My Solution
        n=len(words)
        l=[set(words[i]) for i in range(n)] #here the words with daab are given as ('d','a','b') redundant values are removed so its easy to compute
        maxi=0
        for i in range(n):
            for j in range(i+1,n):
                if not (l[i] & l[j]):
                    #print(l[i],l[j])
                    #dont give l[i] and l[j] , they are length of set values so give words [i] and words[j] respectively.
                    maxi=max(maxi,len(words[i])*len(words[j]))
        return maxi
    
    
    
    
    #Discussed Solution
#     This approach replaces the char_set in above approach using a bit_mask. The set bits of the bit_mask will indicate the presence of a char in the word. This will also help improve the time complexity as the code will replace the & of two hashset which is O(min(len(s1), len(s2)) with & operation between two integers which is O(1).

# class Solution:
#     def maxProduct(self, words: List[str]) -> int:
#         n=len(words)
        
#         bit_masks = [0] * n
#         lengths = [0] * n
        
#         for i in range(n):             
#             for c in words[i]:
#                 bit_masks[i]|=1<<(ord(c) - ord('a')) # set the character bit            
#             lengths[i]=len(words[i])
                        
#         max_val = 0
#         for i in range(n):
#             for j in range(i+1, n):
#                 if not (bit_masks[i] & bit_masks[j]):
#                     max_val=max(max_val, lengths[i] * lengths[j])
        
#         return max_val