"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        l=[]
        def preorder(th):
            if th==None:
                return
            
            for i in th.children:
                preorder(i)
            l.append(th.val)
        preorder(root)
        return l