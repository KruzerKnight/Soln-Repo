# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def kruz(th1,th2):
            if th1==None or th2==None:
                return th1==th2
            elif th1.val!=th2.val:
                return False
            return kruz(th1.left,th2.right) and kruz(th1.right,th2.left)
        return kruz(root.left,root.right)
        
     
 # if one of them is null
 # compare them
 # if above not executed, means they are both number
 # if they are both different return false
 # if they are similar go and look further