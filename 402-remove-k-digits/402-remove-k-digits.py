# In order to get the smallest possible number, we have to get rid of as many as possible big digits in the most significant places on the left. We can use a monotonically increasing stack to help us remove those big digits. When adding a new digit, we check whether the previous one is bigger than the current and pop it out. In the end, we concatenate the remaining elements from the stack and return the result.

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st = list()
        for n in num:
            while st and k and st[-1] > n:
                st.pop()
                k -= 1
            
            if st or n is not '0': # prevent leading zeros
                st.append(n)
                
        if k: # not fully spent
            st = st[0:-k]
            
        return ''.join(st) or '0'