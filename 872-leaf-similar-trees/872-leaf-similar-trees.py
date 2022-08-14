# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def trav(node):
            if node==None:
                return []
            if node.left==None and node.right==None:
                return [node.val]
            return trav(node.left)+trav(node.right)
        return trav(root1)==trav(root2)