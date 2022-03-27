"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        l=[]
        def preorder(th):
            if th==None:
                return
            l.append(th.val)
            for i in th.children:
                preorder(i)
        preorder(root)
        return l