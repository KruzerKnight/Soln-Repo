# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heappush, heappop, heapreplace, heapify
class Solution(object):
    def mergeKLists(self, lists):
    
        dummy = node = ListNode(0)
        h = [(n.val, n) for n in lists if n]
        heapify(h)
        while h:
            v, n = h[0]                 #return the smallest value in the heap  
            if n.next is None:
                heappop(h) #only change heap size when necessary, at a sll's end
            else:
                heapreplace(h, (n.next.val, n.next))     #smallest values is replaced with next
            node.next = n                 
            node = node.next              #result linked lists is created by linking them

        return dummy.next              #the starting node is returned
        