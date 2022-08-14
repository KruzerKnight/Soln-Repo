# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi=float('-inf')
        def maxsum(node):
            if node==None:
                return 0
            left=max(0,maxsum(node.left))
            right=max(0,maxsum(node.right))
            
            self.maxi=max(self.maxi,node.val+left+right)
            return node.val+max(left,right)
        
        return max(maxsum(root),self.maxi)