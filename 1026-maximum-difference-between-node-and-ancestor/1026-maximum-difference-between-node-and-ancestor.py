# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.diff=0
        def kruz(node,maxi,mini):
            if not node:
                return
            self.diff=max(self.diff,abs(maxi-node.val),abs(mini-node.val))
            # print(self.diff,m,node.val)
            maxi=max(maxi,node.val)
            mini=min(mini,node.val)
            kruz(node.left,maxi,mini)
            kruz(node.right,maxi,mini)
            return
        kruz(root,root.val,root.val)
        return self.diff
    
    # Dont focus only on the maximum value in ancestors, focus on the minimum values in ansecstors too, thats the 2nd example