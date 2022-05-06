class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        l=[['kruz',0]]
        for i in s:
            if l[-1][0]==i:
                l[-1][1]+=1
                if l[-1][1]==k:
                    l.pop()
            else:
                l.append([i,1])
        return ''.join(i*j for i,j in l[1:])
    
# Save the character c and its count to the stack.
# If the next character c is same as the last one, increment the count.
# Otherwise push a pair (c, 1) into the stack.
# I used a dummy element ('#', 0) to avoid empty stack.