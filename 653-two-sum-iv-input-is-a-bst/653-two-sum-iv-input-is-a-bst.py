# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def kruz(th,check,k):
            if th==None:
                return False
            if k-th.val in check:
                return True
            check.add(th.val)
            
            return kruz(th.left,check,k) or kruz(th.right,check,k)
        return kruz(root,set(),k)