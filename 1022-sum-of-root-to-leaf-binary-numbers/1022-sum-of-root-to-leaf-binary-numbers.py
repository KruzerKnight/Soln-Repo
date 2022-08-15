# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.sums=0
        def kruz(node,s):
            if node==None:
                return
            s+=str(node.val)
            if node.left==None and node.right==None:
                self.sums+=int(s,2)
                return
            kruz(node.left,s)
            kruz(node.right,s)
            return
        kruz(root,'')
        return self.sums