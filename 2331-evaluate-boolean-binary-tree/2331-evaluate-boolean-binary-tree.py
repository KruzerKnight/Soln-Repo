# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root.val==1 or root.val==0:
            return root.val
        l=self.evaluateTree(root.left)
        r=self.evaluateTree(root.right)
        
        if root.val==2:
            return l|r
        else:
            return l&r