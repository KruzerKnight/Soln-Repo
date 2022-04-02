class Solution:
    def validPalindrome(self, s: str) -> bool:
        def verify(s, left, right, counter=0):
            while left < right:
                if s[left] != s[right]:
                    if counter == 1:
                        return False
                    else:
                        return verify(s, left+1, right, counter+1) or verify(s, left, right-1, counter+1)
                else:
                    left += 1
                    right -= 1
            return True
        return verify(s, 0, len(s)-1)